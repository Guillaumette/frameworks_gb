from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/about/')
def about():
    return '<h1>Обо мне</h1>'


@app.route('/contact/')
def contact():
    return '<h1>Контакты</h1>'


@app.route('/return_num/<int:num>/<int:num1>/')
def return_number(num, num1):
    return str(num + num1)


if __name__ == '__main__':
    app.run(debug=True)