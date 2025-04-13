import pytest
from app import app
import pytest
from app.app import app as flask_app
#app/tests/integration/test_flask_app.py

from flask.testing import FlaskClient


"""
@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client
"""
def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Selecciona la dificultad' in response.data

def test_index_post_redirect(client):
    response = client.post('/', data={'difficulty': '1'}, follow_redirects=False)
    assert response.status_code == 302  # Redirect to /question
    assert '/question' in response.headers['Location']

def test_question_get(client):
    # Primero iniciamos la sesión creando un quiz
    client.post('/', data={'difficulty': '1'})
    response = client.get('/question')
    assert response.status_code == 200
    assert b'Pregunta' in response.data

def test_question_post(client):
    client.post('/', data={'difficulty': '1'})
    response = client.get('/question')  # Obtener una pregunta
    assert response.status_code == 200

    # Simulamos responder la pregunta
    response = client.post('/question', data={'answer': '0'}, follow_redirects=False)
    # Puede ser redirigido a otra pregunta o a /result si ya es la última
    assert response.status_code in [200, 302]

def test_result(client):
    client.post('/', data={'difficulty': '1'})
    # Respondemos todas las preguntas (simplificado para testear resultado)
    for _ in range(10):  # suponiendo que se cargan 10 preguntas
        client.post('/question', data={'answer': '0'})
    response = client.get('/result')
    assert response.status_code == 200
    assert b'Juego terminado' in response.data