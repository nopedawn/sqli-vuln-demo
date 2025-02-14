from flask import Flask, request
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

db_config = {
    'host': os.getenv('HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

@app.route('/')
def home():
    return '''
    <h1>Login</h1>
    <form method="POST" action="/login">
        <input type="text" name="username" placeholder="Username" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit">Login</button>
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = None

    try:
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return f"Login successful! Welcome, {user[1]}."
        else:
            return "Invalid credentials!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)