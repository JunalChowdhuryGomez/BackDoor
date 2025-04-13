from question import Question
from quiz import Quiz
from database import get_questions_from_db

def run_quiz():
    # inicia el objeto Quiz
    quiz = Quiz()
    print("Bienvenido al Quiz de Historia del Peru")
    # solicita el nivel de dificultad
    print("=========================================")
    print("Elige la dificultad del Quiz")
    print("1. Facil")
    print("2. Intermedio")
    print("3. Dificil")
    print("4. Mixto")

    # verifica la entrada del usuario
    while True:
        try:
            # validad la entrada de la dificultad
            nivel = int(input("respuesta >>> "))
            if 1 <= nivel <= 4:
                nivel -= 1
                break
            else:
                print(f"clave no permitida")
        except ValueError:
            print("entrada invalida - vuelvea intentar")
    
    # obtiene las preguntas de la base de datos en base al nivel elegido
    questions = get_questions_from_db()[:10] if nivel == 4 else get_questions_from_db(nivel)[:10]
    for question in questions:
        quiz.add_question(question)

    # inicia el juego
    while True:
        question = quiz.get_next_question()
        if not question:
            break
        print(f"\nPregunta {quiz.current_question_index}: {question.description}")
        for idx, opt in enumerate(question.options):
            print(f"{idx + 1}. {opt}")

        # solicita la respuesta del usuario
        while True:
            # valida la respuesta
            try:
                answer = int(input("respuesta >>> "))
                if 1 <= answer <= len(question.options):
                    answer -= 1  # restamos 1 para que coincida con los índices (0-3)
                    break
                else:
                    print(f"clave no permitida")
            except ValueError:
                print("entrada invalida - vuelvea intentar")
        # verifica si la respuesta es correcta
        if quiz.answer_question(question, answer):
            print("======== Correcto =======")
        else:
            print("======== Incorrecto =======")

    # termina el juego
    # muestra el resultado final
    print()
    print("=========================================") 
    print("============ Juego terminado ============")
    print(f"respuestas Correctas: {quiz.correct_answers}")
    print(f"respuestas Incorrectas: {quiz.incorrect_answers}")
    print("=========================================")

# funcion principal
# inicia el programa
def main():
    print("\nDia 5 - \n ")
    run_quiz()

if __name__ == "__main__":
    main()