import pytest
from question import Question
import unittest




class TestQuestion(unittest.TestCase):

    def test_question_attributes(self):
        description = "¿Cual es 2 + 2?"
        options = ["1", "2", "3", "4"]
        correct_index = 3
        difficulty = 2
        question = Question(description, options, correct_index, difficulty)

        self.assertEqual(question.description, description)
        self.assertEqual(question.options, options)
        self.assertEqual(question.correct_index, correct_index)
        self.assertEqual(question.difficulty, difficulty)

    def test_question_correct_answer(self):
        question = Question("Capital de Francia", ["Madrid", "Londres", "Paris", "Berlin"], 2, 1)
        self.assertTrue(question.is_correct(2))

    def test_question_incorrect_answer(self):
        question = Question("Capital de Francia", ["Madrid", "Londres", "Paris", "Berlin"], 2, 1)
        self.assertFalse(question.is_correct(1))

    def test_question_out_of_range_index(self):
        question = Question("Capital de España", ["Madrid", "Barcelona", "Sevilla", "Valencia"], 0, 1)
        self.assertFalse(question.is_correct(4))  # Índice fuera de rango

    def test_question_invalid_type(self):
        question = Question("2+2?", ["1", "2", "3", "4"], 3, 1)
        with self.assertRaises(TypeError):
            question.is_correct("tres")  # Tipo inválido

if __name__ == '__main__':
    unittest.main()