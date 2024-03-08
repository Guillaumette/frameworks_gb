from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clothing/')
def clothing():
    _clothes = [{'name': 'Кофта',
                 'description': 'Теплая кофта',
                 'price': 'Цена: 500 р.',
                 },
                {'name': 'Штаны',
                 'description': 'Модные, молодежные',
                 'price': 'Цена: 1000 р.',
                 }]
    context = {'clothes': _clothes}
    return render_template('clothing.html', **context)


@app.route('/shoes/')
def shoes():
    _shoes = [{'name': 'Кроссовки',
                 'description': 'Новинка от FILA',
                 'price': 'Цена: 7000 р.',
                 },
                {'name': 'Зимние ботинки',
                 'description': 'Долговечные, для наших реагентов',
                 'price': 'Цена: 5000 р.',
                 }]
    context = {'shoes': _shoes}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run(debug=True)