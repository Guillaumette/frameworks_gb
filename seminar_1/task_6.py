from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/table/')
def table():
    _students = [{'name': 'Анна',
                  'last_name': 'Князева',
                  'age': '29',
                  'avg_mark': '5.0',
                  },
                 {'name': 'Анастасия',
                  'last_name': 'Маневич',
                  'age': '23',
                  'avg_mark': '5.0',
                  },
                 {'name': 'Екатерина',
                  'last_name': 'Петрова',
                  'age': '21',
                  'avg_mark': '4.5',
                  }]

    context = {'students': _students,
               'title': 'Студенты'}
    return render_template('table.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
