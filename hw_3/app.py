from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf import CSRFProtect
from werkzeug.security import generate_password_hash

from hw_3.model import db, User  # Импортируем db и модель User
from hw_3.form import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '3a188ed328ad2953ef5db2b4fffa2dea251d399a962d4e5cb620e1c1a96b7fa4'
csrf = CSRFProtect(app)

# Инициализируем объект db в приложении
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Вы успешно зарегистрировались!")
        return redirect((url_for('register')))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
