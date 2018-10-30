from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegisterForm
from app.models import User, Poster, UserLike, Poster
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
def index():
    posts = Poster.getPosters()
    return render_template('index.html', title='Home', posts=posts)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/posterValidation')
@login_required
def posterValidation():
    return render_template('posterValidation.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.getUserByUsername(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, validated=False)
        user.set_password(form.password.data)
        user.addUser()
        flash('Usuario registrado con éxito. Debes esperar a que un administrador te valide para poder hacer Log In')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/poster')
@login_required
def poster():
    return render_template('poster.html')

@app.route('/adminProfile')
@login_required
def adminProfile():
    return render_template('adminProfile.html')

@app.route('/like')
@login_required
def like():
    pass
    return render_template('index.html')