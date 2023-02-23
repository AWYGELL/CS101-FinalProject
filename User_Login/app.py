from flask import Flask, request, session, redirect, url_for, render_template
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static')

# Secret key for session
app.secret_key = 'secret_key'

# Database connection
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)''')
conn.commit()

# Home page (login/register)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Login':
            # Check if user exists in database
            username = request.form['username']
            password = request.form['password']
            c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = c.fetchone()
            if user:
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                return render_template('home.html', message='Incorrect username or password')
        elif request.form['submit_button'] == 'Register':
            # Add new user to database
            username = request.form['username']
            password = request.form['password']
            c.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = c.fetchone()
            if user:
                return render_template('home.html', message='Username already exists')
            else:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                session['username'] = username
                return redirect(url_for('dashboard'))

    return render_template('home.html')


# Dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
