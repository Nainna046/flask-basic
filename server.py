from flask import Flask, app

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/name')
def name():
    return f'<h1>Natthawut</h1>'


if __name__ == '__main__':
    app.run(debug=True)

    