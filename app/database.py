import psycopg2
import random
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from question import Question
load_dotenv(".env")

# refactorizamos el metodo get_questions_from_db para que reciba un parameto opcional difficulty
def get_questions_from_db(difficulty=None):
    # validadmos que la dificulatad este entre 1 y 3
    if difficulty is not None and difficulty not in [1, 2, 3]:
        raise ValueError("La dificultad debe ser 1, 2 o 3")
    
    # connexion a la bd "trivia_db"  de postgres
    connection = psycopg2.connect(
        dbname="trivia_db",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )
    cursor = connection.cursor()
    # hacemos la consulta 
    if difficulty is not None:
        # hacemos la consulta si no se pasa la dificultad
        cursor.execute("""
            SELECT description, option_1, option_2, option_3, option_4, correct_option_index, difficulty
            FROM questions
            WHERE difficulty = %s;
        """, (difficulty,))
    else:
        # hacemos la consulta si  se pasa la dificultad
        cursor.execute("""
            SELECT description, option_1, option_2, option_3, option_4, correct_option_index, difficulty
            FROM questions;
        """)

    rows = cursor.fetchall()
    connection.close()

    # creamos lista de "question" con los datos traidos de la bd
    questions = [
        Question(row[0], row[1:5], row[5], row[6])
        for row in rows
    ]
    # mezclamos las preguntas
    #random.shuffle(questions)
    return questions