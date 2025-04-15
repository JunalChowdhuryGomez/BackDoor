import unittest
from unittest.mock import patch
from main import seleccionar_dificultad, obtener_respuesta_valida, mostrar_pregunta, mostrar_resultados
from question import Question
from quiz import Quiz

class TestMainFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=['2'])
    def test_seleccionar_dificultad_valida(self, mock_input):
        # Debe devolver 1 (porque se resta 1 internamente)
        self.assertEqual(seleccionar_dificultad(), 1)

    @patch('builtins.input', side_effect=['abc', '10', '1'])
    def test_seleccionar_dificultad_invalida(self, mock_input):
        # Simula entrada inválida (texto), número fuera de rango y luego válida
        self.assertEqual(seleccionar_dificultad(), 0)

    @patch('builtins.input', side_effect=['3'])
    def test_obtener_respuesta_valida_valida(self, mock_input):
        self.assertEqual(obtener_respuesta_valida(4), 2)  # 3 - 1 = 2

    @patch('builtins.input', side_effect=['x', '5', '2'])
    def test_obtener_respuesta_valida_invalida(self, mock_input):
        self.assertEqual(obtener_respuesta_valida(3), 1)

    def test_mostrar_pregunta_output(self):
        question = Question("¿Capital del Perú?", ["Lima", "Cusco", "Arequipa", "Trujillo"], 0, 1)
        quiz = Quiz()
        quiz.current_question_index = 1
        with patch('builtins.print') as mock_print:
            mostrar_pregunta(quiz, question)
            mock_print.assert_any_call("Pregunta 1: ¿Capital del Perú?")

    def test_mostrar_resultados(self):
        quiz = Quiz()
        quiz.correct_answers = 3
        quiz.incorrect_answers = 2
        with patch('builtins.print') as mock_print:
            mostrar_resultados(quiz)
            mock_print.assert_any_call("respuestas Correctas: 3")
            mock_print.assert_any_call("respuestas Incorrectas: 2")

if __name__ == '__main__':
    unittest.main()
