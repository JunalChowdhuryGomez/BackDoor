import psycopg2
import random
from question import Question

def get_questions_from_db(difficulty=None):
    if difficulty is not None and difficulty not in [1, 2, 3]:
        raise ValueError("La dificultad debe ser 1, 2 o 3")

    connection = psycopg2.connect(
        dbname="trivia_db",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )
    cursor = connection.cursor()

    if difficulty is not None:
        cursor.execute("""
            SELECT description, option_1, option_2, option_3, option_4, correct_option_index, difficulty
            FROM questions
            WHERE difficulty = %s;
        """, (difficulty,))
    else:
        cursor.execute("""
            SELECT description, option_1, option_2, option_3, option_4, correct_option_index, difficulty
            FROM questions;
        """)

    rows = cursor.fetchall()
    connection.close()

    questions = [
        Question(row[0], row[1:5], row[5], row[6])
        for row in rows
    ]
    
    random.shuffle(questions)
    return questions
