import pytest

from app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    app.secret_key = 'dev'  # Necesario para usar sesiones en tests

    with app.test_client() as client:
        with app.app_context():
            yield client

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        difficulty = int(request.form['difficulty'])
        questions = get_questions_from_db(difficulty)[:10]
        quiz = Quiz()
        for q in questions:
            quiz.add_question(q)
        session['quiz'] = save_quiz(quiz)
        return redirect(url_for('question'))
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    quiz = restore_quiz(session['quiz'])
    if request.method == 'POST':
        answer = int(request.form['answer'])
        current_question = quiz.questions[quiz.current_question_index - 1]
        quiz.answer_question(current_question, answer)

    next_question = quiz.get_next_question()
    if next_question is None:
        session['quiz'] = save_quiz(quiz)
        return redirect(url_for('result'))

    session['quiz'] = save_quiz(quiz)
    return render_template('question.html', question=next_question, index=quiz.current_question_index)

@app.route('/result')
def result():
    if 'quiz' not in session:
        return redirect(url_for('index'))
    quiz = restore_quiz(session['quiz'])
    return render_template('result.html', correct=quiz.correct_answers, incorrect=quiz.incorrect_answers)
