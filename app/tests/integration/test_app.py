import pytest
from app import app, save_quiz, restore_quiz
from quiz import Quiz
from question import Question
import unittest
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as session:
            session.clear()
        yield client
client = app.test_client()
class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Selecciona la dificultad", response.data)


    def test_save_and_restore_quiz(self):
        quiz = Quiz()
        q1 = Question("¿Capital del Perú?", ["Lima", "Cusco", "Arequipa", "Trujillo"], 0, "Facil")
        quiz.add_question(q1)
        quiz.correct_answers = 1
        quiz.incorrect_answers = 0
        quiz.current_question_index = 1

        data = save_quiz(quiz)
        restored_quiz = restore_quiz(data)

        self.assertEqual(restored_quiz.correct_answers, 1)
        self.assertEqual(restored_quiz.questions[0].description, "¿Capital del Perú?")


