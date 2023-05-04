from flask import Flask, render_template, request, send_file
import sqlite3

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    
    conn = sqlite3.connect('database.db')    
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return 'Form submitted successfully!'

@app.route('/secretcode')
def download_file():
    filename = 'database.db'  
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
