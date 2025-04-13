import pytest
from question import Question

# test 
def test_question_correct_answer():
    question = Question("Capital de Francia", ["Madrid", "Londres", "Paris", "Berlin"], 2, 1)
    assert question.is_correct(2)

#
def test_question_incorrect_answer():
    question = Question("Capital de Francia", ["Madrid", "Londres", "Paris", "Berlin"], 2, 1)
    assert not question.is_correct(1)

def test_question_out_of_range_index():
    question = Question("Capital de Espana", ["Madrid", "Barcelona", "Sevilla", "Valencia"], 0, 1)
    assert not question.is_correct(4)

def test_question_invalid_type():
    question = Question("2+2?", ["1", "2", "3", "4"], 3, 1)
    with pytest.raises(TypeError):
        question.is_correct("tres") 

def test_question_attributes():
    description = "¿Cual es 2 + 2?"
    options = ["1", "2", "3", "4"]
    correct_index = 3
    difficulty = 2
    question = Question(description, options, correct_index, difficulty)

    assert question.description == description
    assert question.options == options
    assert question.correct_index == correct_index
    assert question.difficulty == difficulty
