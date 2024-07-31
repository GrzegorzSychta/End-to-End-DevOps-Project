from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/tables.html')
def tables():
    return render_template('tables.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/password.html')
def forgot_password():
    return render_template('password.html')

if __name__ == '__main__':
    app.run

test = "Test ArgoCD changes."

