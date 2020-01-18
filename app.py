from flask import Flask, session, send_from_directory, render_template
from flask_session import Session
import os
app = Flask(__name__)
SESSION_TYPE = 'sqlalchemy'
app.secret_key = os.urandom(24)
app.config.from_object(__name__)
Session(app)

questions = [
    {
        'file': '1.jpg',
        'answers': ['cat', 'crete cat', 'dog'],
        'query': 'The question is can you find this with >99% accuracy?',
        'hint': 'Is it a cat or a dog?'
    },
    {
        'file': '2.png',
        'answers': ['tux'],
        'query': 'Not just any penguin!',
        'hint': 'The Linux Mascot!'
    },
    {
        'file': '3.png',
        'answers': ['fedora hat', 'fedora'],
        'query': 'And this is not just any hat',
        'hint': 'Has the same name as a popular linux distro'
    },
    {
        'file': '4.png',
        'answers': ['fedora project', 'fedora'],
        'query': 'Who said that this is not a hat?',
        'hint': 'The GCI organisation with the most tasks solved'
    },
    {
        'file': '5.jpg',
        'answers': ['flask', 'python flask'],
        'query': 'Hint: This is a hard one. FFFFFFFFound it yet?',
        'hint': 'A python framework that was used to make this app'
    },
    {
        'file': '6.jpeg',
        'answers': ['linus torvalds'],
        'query': 'Doesn\'t he look lovely?',
        'hint': 'The founder of Linux'
    },
    {
        'file': '7.png',
        'answers': ['fedora pagure', 'pagure'],
        'query': 'Don\t. Be. Like. A. Snail. Answer. Quickly.',
        'hint': 'Github but good'
    },
    {
        'file': '8.png',
        'answers': ['gnome project', 'gnome desktop', 'gnome'],
        'query': 'What is this insane multitasking?',
        'hint': 'The default desktop environment on many distros'
    },
    {
        'file': '9.png',
        'answers': ['shebang', 'hashbang'],
        'query': 'Wait a minute, I\'ve seen this before',
        'hint': 'The starting line for scripts on linux'
    },
    {
        'file': '10.jpg',
        'answers': ['ibm pc 5150', '5150'],
        'query': 'Wow, who\'s old now?',
        'hint': 'The model number of the first IBM PC'
    }
]

@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('images', path)


@app.route('/')
def index():
    if 'qid' not in session:
        session['qid']=0

    current_qid = session['qid']
    print(current_qid)
    if current_qid>=len(questions):
        session['qid'] = 0
        return 'Game Finished'
        return render_template('complete.html')
    return render_template("show_question.html", image_path=questions[current_qid]['file'], query_text=questions[current_qid]['query'], correct_answers=questions[current_qid]['answers'], hint=questions[current_qid]['hint'])

@app.route('/next_question')
def next_question():
    session['qid'] +=1
    return 'OK'  

@app.route('/game_over')
def game_over():
    session['qid'] = 0
    return 'You need to start over :('


if __name__ == '__main__':
    app.run(debug=True)
