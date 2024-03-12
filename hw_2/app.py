from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    name = request.form.get('name')
    email = request.form.get('email')

    response = make_response(render_template('login.html', name=name))
    response.set_cookie('user_data', f'name={name}&email={email}')

    return response


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', '', expires=0)

    return response


if __name__ == '__main__':
    app.run(debug=True)
