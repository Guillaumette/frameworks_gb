"""
Хранение данных
В финале лекции рассмотрим возможность сохранения данных между запросами.
Работа с cookie файлами в Flask
Cookie файлы — это небольшие текстовые файлы, которые хранятся в браузере
пользователя и используются для хранения информации о пользователе и его
предпочтениях на сайте. В Flask, работа с cookie файлами очень проста и может
быть выполнена с помощью самого фреймворка, без установки дополнительных
модулей.
Для работы с cookie файлами, необходимо импортировать модуль Flask и объект
request, который позволяет получить доступ к cookie файлам. Подобное мы
проделывали несколько раз за лекцию.
"""
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response('Cookie установлен')
    response.set_cookie('username', 'admin')
    return response


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f'Значение cookie: {name}'


if __name__ == '__main__':
    app.run(debug=True)
