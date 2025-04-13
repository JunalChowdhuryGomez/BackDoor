class Question:
    def __init__(self, description, options, correct_index, difficulty):
        self.description = description
        self.options = options
        self.correct_index = correct_index
        self.difficulty = difficulty

    def is_correct(self, answer_index):
        if not isinstance(answer_index, int):
            raise TypeError("answer_index debe ser un entero")
        return self.correct_index == answer_index
