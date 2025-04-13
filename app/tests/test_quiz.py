import pytest
from quiz import Quiz
from question import Question

# test para comprobar metodo add_question de la clase Quiz
def test_add_question():
    quiz = Quiz()
    q = Question("Capital de Peru?", ["Paris", "Lima", "Madrid", "Berlin"], 1, 1)
    quiz.add_question(q)
    # verifica la insercion de la pregunta
    assert len(quiz.questions) == 1
    # verifica el atributo description de la pregunta
    assert quiz.questions[0].description == "Capital de Peru?"

# test para verificar el funcionamiento del metodo get_next_question con preguntas agregadas  
def test_get_next_question_returns_correctly():
    quiz = Quiz()
    q1 = Question("pregunta prueba 1", ["A", "B", "C", "D"], 0, 1)
    q2 = Question("pregunta prueba 2", ["A", "B", "C", "D"], 1, 2)
    # se aggrega 2 preguntas de prueba
    quiz.add_question(q1)
    quiz.add_question(q2)
    # se verifica que funcione el metodo get_next_question
    assert quiz.get_next_question() == q1
    assert quiz.get_next_question() == q2

# test para verificar el funcionamiento del metodo get_next_question sin preguntas agregadas  
def test_get_next_question_returns_none_when_empty():
    quiz = Quiz()
    # se verifica que no devuelva nada cuando no hay preguntas agregadas
    assert quiz.get_next_question() is None

# test para verificar el funcionamiento del metodo get_next_question cuando se acabban las preguntas
def test_get_next_question_returns_none_after_all_questions():
    quiz = Quiz()
    q1 = Question("pregunta prueba", ["A", "B", "C", "D"], 1, 3)
    # se agrega 1 pregunta de prueba
    quiz.add_question(q1)

    quiz.get_next_question()  # devuelve la pregunta (deberia ser el unico pregunta)
    assert quiz.get_next_question() is None  # devuelve None (ya no habria pregunta)


def test_quiz_scoring():
    quiz = Quiz()
    question = Question("pregunta prueba", ["A", "B", "C", "D"], 3, 1) 
    quiz.add_question(question)
    
    assert quiz.answer_question(question, 3) == True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0

def test_quiz_incorrect_answer():
    quiz = Quiz()
    question = Question("pregunta prueba", ["A", "B", "C", "D"], 2, 1)
    quiz.add_question(question)

    assert quiz.answer_question(question, 1) == False  # Respuesta incorrecta
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1
