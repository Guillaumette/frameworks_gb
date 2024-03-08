from flask import Flask

app = Flask(__name__)

# Множественное декорирование
@app.route('/Фёдор/')
@app.route('/Федор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'


if __name__ == '__main__':
    app.run(debug=True)
