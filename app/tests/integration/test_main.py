import unittest
from unittest.mock import patch
from main import seleccionar_dificultad, obtener_respuesta_valida, mostrar_pregunta, mostrar_resultados, run_quiz
from question import Question
from quiz import Quiz
from io import StringIO

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


    
    @patch('builtins.input', side_effect=['2'])  # Usuario elige "Intermedio"
    def test_seleccionar_dificultad(self, mock_input):
        dificultad = seleccionar_dificultad()
        self.assertEqual(dificultad, 1)  # 2 - 1 = 1 (Intermedio)

    @patch('builtins.input', side_effect=['4'])  # Usuario elige la opción 4
    def test_obtener_respuesta_valida(self, mock_input):
        respuesta = obtener_respuesta_valida(4)
        self.assertEqual(respuesta, 3)  # 4 - 1 = 3 (índice base 0)

    @patch('builtins.input', side_effect=[
        '1',  # dificultad: Fácil
        '1',  # respuesta a pregunta 1
        '2',  # respuesta a pregunta 2
        '3',  # respuesta a pregunta 3
        '4',  # respuesta a pregunta 4
        '1',  # ...
        '1',
        '1',
        '1',
        '1',
        '1'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('main.get_questions_from_db')
    def test_run_quiz_flujo_completo(self, mock_get_questions, mock_stdout, mock_input):
        # Preparamos 10 preguntas de prueba
        from question import Question
        preguntas_mock = [
            Question(
                description=f"Pregunta {i+1}",
                options=["a", "b", "c", "d"],
                correct_index=0,
                difficulty=1
            ) for i in range(10)
        ]
        mock_get_questions.return_value = preguntas_mock

        run_quiz()

        salida = mock_stdout.getvalue()
        self.assertIn("Juego terminado", salida)
        self.assertIn("respuestas Correctas", salida)
        self.assertIn("respuestas Incorrectas", salida)



if __name__ == '__main__':
    unittest.main()
