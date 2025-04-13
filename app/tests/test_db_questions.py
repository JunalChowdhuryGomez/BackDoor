from database import get_questions_from_db
import pytest
from unittest.mock import patch, MagicMock
from database import get_questions_from_db
from question import Question



# test:verifica la conectividad con la base datos y la obtencion de preguntas (se asume que hay al menos hay una pregunta en la base de datos)
def test_get_questions_from_db_returns_list():
    questions = get_questions_from_db()
    assert isinstance(questions, list)
    assert all(hasattr(q, 'description') for q in questions)

@patch("database.psycopg2.connect")
def test_get_questions_from_db_with_valid_difficulty(mock_connect):
    # Simula conexión y cursor
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        ("¿Capital de Francia?", "Londres", "París", "Madrid", "Roma", 1, 1),
        ("¿2 + 2?", "1", "2", "3", "4", 3, 1),
    ]
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_connection

    questions = get_questions_from_db(1)

    assert len(questions) == 2
    assert all(isinstance(q, Question) for q in questions)
    assert questions[0].difficulty == 1

@patch("database.psycopg2.connect")
def test_get_questions_from_db_with_invalid_difficulty(mock_connect):
    with pytest.raises(ValueError):
        get_questions_from_db(5)

@patch("database.psycopg2.connect")
def test_get_questions_from_db_without_difficulty(mock_connect):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        ("Pregunta prueba", "A", "B", "C", "D", 0, 2)
    ]
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_connection

    questions = get_questions_from_db()
    assert len(questions) == 1
    assert questions[0].description == "Pregunta prueba"