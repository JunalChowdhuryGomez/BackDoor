import pytest
from app import app

# app/tests/integration/test_flask_app.py

from flask.testing import FlaskClient

def test_index_get():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Selecciona la dificultad:" in response.data

def test_index_post_redirects_to_question():
    client: FlaskClient = app.test_client()
    
    # Esto asume que hay al menos 10 preguntas de dificultad 1
    response = client.post('/', data={'difficulty': '1'}, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Pregunta" in response.data or b"respuesta" in response.data  # Ajusta al texto que aparece en tu template

def test_result_without_session_redirects_to_index():
    client = app.test_client()
    response = client.get('/result')
    assert response.status_code == 302  # Redirect
    assert '/?' in response.location or '/' in response.location
