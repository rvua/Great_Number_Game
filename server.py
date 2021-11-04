import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keepthissecret'

@app.route('/')
def index():
    session['random_number'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    if 'guess' in session:
        if session['guess'] == session['random_number']:
            return redirect('/guessgame')
        elif session['guess'] > session['random_number']:
            return redirect('/guessgame')
        else:
            return redirect('/guessgame') 

@app.route('/guessgame')
def guessgame():
    return render_template('guessgame.html')

@app.route('/play_again')
def play_again():
    session.clear
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)