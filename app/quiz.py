from question import Question

class Quiz:
    def __init__(self): 
        self.questions = []  # Lista de preguntas
        self.current_question_index = 0  # Índice de la pregunta actual
        self.correct_answers = 0  # Contador de respuestas correctas
        self.incorrect_answers = 0  # Contador de respuestas incorrectas

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer_index):
        if question.is_correct(answer_index):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
