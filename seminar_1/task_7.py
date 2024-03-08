from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/news/')
def news():
    _news = [{'title': 'Breaking news!',
             'content': 'The cat slept well and happy!',
              'date': '2024-03-08',
              },
             {'title': 'Good news!',
              'content': 'Communism is coming!',
              'date': '2024-03-09',
              }]
    context = {'news': _news,
               'title': 'Новостная страница'}
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run(debug=True)