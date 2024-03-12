"""
Перенаправления в Framework Flask позволяют перенаправлять пользователя с
одной страницы на другую.
Это может быть полезно, например, для перенаправления пользователя
после успешной отправки формы или для перенаправления пользователя
на страницу авторизации при попытке доступа к
защищенной странице без авторизации.

Для перенаправления в Flask используется функция redirect().
Она принимает URL-адрес, на который нужно перенаправить пользователя,
и возвращает объект ответа,
который перенаправляет пользователя на указанный адрес.

redirect() в Flask - это функция, которая используется для перенаправления
пользователя на другую страницу. При вызове redirect() вы указываете адрес,
на который нужно направить пользователя,
и Flask автоматически делает перенаправление на эту страницу.

Например, если у вас есть маршрут /home и вы хотите перенаправить
пользователя на этот маршрут из другой функции представления,
вы можете использовать redirect(url_for('home')),
где url_for('home') возвращает URL для маршрута /home.
"""
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external')
def external_redirect():
    return redirect('https://google.com')


@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run(debug=False)
