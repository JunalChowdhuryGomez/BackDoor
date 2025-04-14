import pytest
from app import app, save_quiz, restore_quiz
from quiz import Quiz
from question import Question
import unittest
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as session:
            session.clear()
        yield client

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Selecciona la dificultad", response.data)

def test_index_post(client, monkeypatch):
    """Prueba el envío del formulario de dificultad"""
    # Mock de la función que obtiene preguntas
    def mock_get_questions(difficulty):
        return [Question("Pregunta test", ["Op1", "Op2"], 0, difficulty)]
    
    monkeypatch.setattr('app.get_questions_from_db', mock_get_questions)
    
    response = client.post('/', data={'difficulty': '1'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Pregunta test" in response.data

def test_question_flow(client, monkeypatch):
    """Prueba el flujo completo de preguntas y respuestas"""
    # Configurar un quiz en la sesión
    with client.session_transaction() as session:
        quiz = Quiz()
        quiz.add_question(Question("P1", ["A", "B"], 0, 1))
        quiz.add_question(Question("P2", ["C", "D"], 1, 1))
        session['quiz'] = save_quiz(quiz)
    
    # Primera pregunta
    response = client.get('/question')
    assert b"P1" in response.data
    
    # Responder primera pregunta
    response = client.post('/question', data={'answer': '0'}, follow_redirects=True)
    assert b"P2" in response.data
    
    # Responder segunda pregunta
    response = client.post('/question', data={'answer': '1'}, follow_redirects=True)
    assert b"Juego terminado" in response.data
    assert b"Respuestas correctas: 2" in response.data