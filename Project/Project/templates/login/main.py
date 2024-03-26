from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

users = {
    'john': {
        'password': 'password123',
    },
    'jane': {
        'password': 'password',
    }
}


def verify_password(user_password, stored_password_hash):
    return bcrypt.checkpw(user_password.encode('utf-8'), stored_password_hash)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and verify_password(password, users[username]['password']):
            session['username'] = username
            return redirect(url_for('welcome'))

        return "Invalid credentials. Please try again."

    return render_template('login.html')


@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return f"Welcome, {username}!"
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Clear the session data upon logout
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['f_name']
        lastname = request.form['l_name']
        phoneno = request.form['p_number']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username in users:
            return "Username already taken. Please choose a different username."

        if password != confirm_password:
            return "Passwords do not match. Please try again."

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users[username] = {
            'password_hash': hashed_password,
            'firstname': firstname,
            'lastname': lastname,
            'phoneno': phoneno
        }

        # Successful signup, redirect to the login page
        return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
