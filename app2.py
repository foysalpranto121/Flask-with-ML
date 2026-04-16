from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return render_template('form.html', error="Please fill all fields")

    if username == "admin" and password == "12345":
        # Redirect to dashboard with username
        return redirect(url_for('dashboard', user=username))
    else:
        return render_template('form.html', error="Invalid credentials")

@app.route('/dashboard')
def dashboard():
    username = request.args.get('user')
    if not username:
        return redirect(url_for('login'))
    return render_template('login_success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)