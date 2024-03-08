from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/str_length/<string>')
def str_length(string):
    return str(len(string))


if __name__ == '__main__':
    app.run(debug=True)