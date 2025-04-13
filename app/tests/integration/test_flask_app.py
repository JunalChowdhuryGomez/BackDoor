import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Selecciona dificultad" in response.data  # texto del index.html

def test_index_post_redirect(client):
    response = client.post('/', data={'difficulty': 1}, follow_redirects=False)
    assert response.status_code == 302  # Redirección a /question

def test_question_flow(client):
    # Comienza seleccionando dificultad
    client.post('/', data={'difficulty': 1})
    # Obtiene primera pregunta
    response = client.get('/question')
    assert response.status_code == 200
    assert b"Pregunta" in response.data  # Validar que renderiza pregunta
