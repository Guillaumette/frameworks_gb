from flask import Flask
from flask_wtf import FlaskForm, CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'3a188ed328ad2953ef5db2b4fffa2dea251d399a962d4e5cb620e1c1a96b7fa4'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)
