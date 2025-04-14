import unittest
from quiz import Quiz
from question import Question

# test para comprobar metodo add_question de la clase Quiz
class TestQuiz(unittest.TestCase):

    def test_add_question(self):
        quiz = Quiz()
        q = Question("Capital de Peru?", ["Paris", "Lima", "Madrid", "Berlin"], 1, 1)
        quiz.add_question(q)
        self.assertEqual(len(quiz.questions), 1)
        self.assertEqual(quiz.questions[0].description, "Capital de Peru?")

    def test_get_next_question_returns_correctly(self):
        quiz = Quiz()
        q1 = Question("pregunta prueba 1", ["A", "B", "C", "D"], 0, 1)
        q2 = Question("pregunta prueba 2", ["A", "B", "C", "D"], 1, 2)
        quiz.add_question(q1)
        quiz.add_question(q2)
        self.assertEqual(quiz.get_next_question(), q1)
        self.assertEqual(quiz.get_next_question(), q2)

    def test_get_next_question_returns_none_when_empty(self):
        quiz = Quiz()
        self.assertIsNone(quiz.get_next_question())

    def test_get_next_question_returns_none_after_all_questions(self):
        quiz = Quiz()
        q1 = Question("pregunta prueba", ["A", "B", "C", "D"], 1, 3)
        quiz.add_question(q1)
        quiz.get_next_question()  # consume la pregunta
        self.assertIsNone(quiz.get_next_question())

    def test_quiz_scoring(self):
        quiz = Quiz()
        question = Question("pregunta prueba", ["A", "B", "C", "D"], 3, 1)
        quiz.add_question(question)
        self.assertTrue(quiz.answer_question(question, 3))
        self.assertEqual(quiz.correct_answers, 1)
        self.assertEqual(quiz.incorrect_answers, 0)

    def test_quiz_incorrect_answer(self):
        quiz = Quiz()
        question = Question("pregunta prueba", ["A", "B", "C", "D"], 2, 1)
        quiz.add_question(question)
        self.assertFalse(quiz.answer_question(question, 1))
        self.assertEqual(quiz.correct_answers, 0)
        self.assertEqual(quiz.incorrect_answers, 1)

if __name__ == '__main__':
    unittest.main()