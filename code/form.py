from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

FORMS = {}

LANGUAGES = [
    'C',
    'Java'
]

def connect():
    db = sqlite3.connect('info.db')
    db.row_factory = sqlite3.Row  # Para acessar por nome
    return db

def init_db():
    db = connect()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS info (
        name TEXT, 
        email TEXT, 
        language TEXT
    )''')
    db.commit()
    cursor.close()
    db.close()


init_db()

@app.route('/')
def index():
    return render_template('login.html', languages=LANGUAGES)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    languages = request.form.getlist('language')
    email = request.form.get('email')
    
    if not name or not email or not languages:
        return render_template('error.html')
    
    for language in languages:
        if language not in LANGUAGES:
            return render_template('erro.html')
    
    db = connect()
    cursor = db.cursor()

    for language in languages:
        cursor.execute(
            "INSERT INTO info (name, email, language) VALUES(?, ?, ?)",
            (name, email, language)
        )
    
    db.commit()
    
    cursor.close()
    db.close()
    
    return redirect('/ok')

@app.route('/ok')
def ok():
    db = connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM info')
    forms = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return render_template('ok.html', forms=forms)

if __name__ == '__main__':
    app.run(debug=True)