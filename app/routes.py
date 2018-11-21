from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegisterForm, ValidateUserForm, ValidatePosterForm, PosterForm, DeletePosterForm, QuestionForm, StatForm, ResponseForm
from app.models import User, Poster, UserLike, Poster, QuestionOption, QuestionOption2, Pregunta, Stat, UserResponse
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/uploadPoster', methods=['GET', 'POST'])
def index():
    form = PosterForm()
    formResponse = ResponseForm()
    posts = Poster.getPostersChecked()
    questions={}
    for post in posts:
        questions[post.id]=QuestionOption.getOpcionPreguntaByPosterId(post.id)
    if formResponse.validate_on_submit():
        options = QuestionOption.getOpcionPreguntaByPosterId(formResponse.id.data)
        print("A CONTINUACION ID POSTER")
        print(formResponse.id.data)
        if formResponse.opcion1:
            if (current_user.is_authenticated):
                respuesta = UserResponse(id_usuario=current_user.id, id_poster = formResponse.id.data, opcion=options[0].opcion)
            else:
                respuesta = UserResponse(id_poster = formResponse.id.data, opcion=options[0].opcion)
            respuesta.addUserResponse()

        if formResponse.opcion2.data:
            if (current_user.is_authenticated):
                respuesta = UserResponse(id_usuario=current_user.id, id_poster = formResponse.id.data, opcion=options[1].opcion)
            else:
                respuesta = UserResponse(id_poster = formResponse.id.data, opcion=options[1].opcion)
            respuesta.addUserResponse()

        if formResponse.opcion3.data:
            if (current_user.is_authenticated):
                respuesta = UserResponse(id_usuario=current_user.id, id_poster = formResponse.id.data, opcion=options[2].opcion)
            else:
                respuesta = UserResponse(id_poster = formResponse.id.data, opcion=options[2].opcion)
            respuesta.addUserResponse()

        if formResponse.opcion4.data:
            if (current_user.is_authenticated):
                respuesta = UserResponse(id_usuario=current_user.id, id_poster = formResponse.id.data, opcion=options[3].opcion)
            else:
                respuesta = UserResponse(id_poster = formResponse.id.data, opcion=options[3].opcion)
            respuesta.addUserResponse()
        if (current_user.is_anonymous):
            return redirect(url_for('stat'))
        else:
            stat = Stat.getUsers(current_user.id)
            if (stat is not None ):
                return redirect(url_for('index'))
            else:
                return redirect(url_for('stat'))
    if form.validate_on_submit():
        post = Poster(id_usuario=current_user.id, titulo=form.titulo.data, corregido=0, imagen=form.imagen.data, reto=form.reto.data, info=form.info.data, pregunta=form.pregunta.data)
        post.addPoster()
        resp1 = QuestionOption(id_poster=post.id,opcion=form.respuesta1.data)
        resp2 = QuestionOption(id_poster=post.id,opcion=form.respuesta2.data)
        resp3 = QuestionOption(id_poster=post.id,opcion=form.respuesta3.data)
        resp4 = QuestionOption(id_poster=post.id,opcion=form.respuesta4.data)       
        resp1.addOpcionPregunta()
        resp2.addOpcionPregunta()
        resp3.addOpcionPregunta()
        resp4.addOpcionPregunta()
        flash('Poster almacenado con éxito. Debes esperar a que un administrador lo corrija para que se pueda mostrar')
        return redirect(url_for('index'))

    return render_template('index.html', title='Home', posts=posts, form=form, formResponse=formResponse,questions=questions)

@app.route('/profile')
@login_required
def profile():
    if current_user.tipo_usuario == 1:
        return redirect(url_for('adminProfile'))
    posts = Poster.getPosterByUserId(current_user.id)
    return render_template('profile.html', title='Profile', posts=posts)

@app.route('/posterValidation/<int:poster_id>')
@login_required
def posterValidation(poster_id):
    post=Poster.getPosterById(poster_id)
    if post.corregido!=0:
        return redirect(url_for('adminProfile'))
    form =  ValidatePosterForm()
    questions = QuestionOption.getOpcionPreguntaByPosterId(poster_id)
    return render_template('posterValidation.html', posts=post, form=form, questions=questions)

@app.route('/poster/<int:poster_id>')
@login_required
def poster(poster_id):
    post = Poster.getPosterById(poster_id)
    form =  ValidatePosterForm()
    questions = QuestionOption.getOpcionPreguntaByPosterId(poster_id)
    return render_template('poster.html', posts=post, form=form, questions=questions)

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
    print("Hola\n")
    if current_user.is_authenticated:
        print("Hola2\n")
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,  nombre=form.nombre.data, apellidos=form.apellidos.data, nia=form.nia.data, validated=False)
        user.set_password(form.password.data)
        user.addUser()
        flash('Usuario registrado con éxito. Debes esperar a que un administrador te valide para poder hacer Log In')
        return redirect(url_for('signup'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/addQuestion', methods=['GET', 'POST'])
@login_required
def addQuestion():
    if current_user.tipo_usuario!=1:
        return redirect(url_for('index'))
    form = QuestionForm()
    if form.validate_on_submit():
        pregunta = Pregunta(pregunta=form.pregunta.data, year=form.year.data)
        pregunta.addPregunta()
        QuestionOption2.newOption(pregunta.id,form.respuesta1.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta8.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta7.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta6.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta5.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta4.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta3.data)    
        QuestionOption2.newOption(pregunta.id,form.respuesta2.data)    
        flash('Pregunta añadida correctamente')
        return redirect(url_for('adminProfile'))
    return render_template('addQuestion.html', title='Nueva Pregunta', form=form)

@app.route('/adminProfile')
@login_required
def adminProfile():
    users = User.getUsersNotValidated()
    form = ValidateUserForm()
    form2 = DeletePosterForm()
    posters = Poster.getPostersNotChecked()
    allposters = Poster.getPosters()
    return render_template('adminProfile.html', users=users, posters=posters, form=form, allposters=allposters, form2=form2)

    
@app.route('/validateUser', methods=['GET', 'POST'])
@login_required
def validateUser():
    if current_user.tipo_usuario != 1:
        return render_template('index.html')
    else:
        form = ValidateUserForm()
        if form.validate_on_submit:
            user = User.getUserByUsername(username=form.user.data)
            if form.action.data == 'validate':
                user.validate()
            elif form.action.data == 'invalidate':
                user.removeUser()
        return redirect(url_for('adminProfile'))

@app.route('/deletePoster', methods=['GET', 'POST'])
@login_required
def deletePoster():
    if current_user.tipo_usuario != 1:
        return render_template('index.html')
    else:
        form = DeletePosterForm()
        if form.validate_on_submit:
            post = Poster.getPosterById(id=form.id.data)
            if form.action.data == 'delete':
                post.removePoster()
        return redirect(url_for('adminProfile'))

@app.route('/posterValidation/validatePoster', methods=['GET', 'POST'])
@login_required
def validatePoster():
    if current_user.tipo_usuario != 1:
        return render_template('index.html')
    else:
        print("Hola\n")
        form = ValidatePosterForm()
        if form.validate_on_submit:
            poster = Poster.getPosterById(id=form.id.data)
            if form.action.data == 'validate':
                poster.validate()
            elif form.action.data == 'invalidate':
                poster.denyPoster()
        return redirect(url_for('adminProfile'))


@app.route('/like')
@login_required
def like():
    pass
    return render_template('index.html')

@app.route('/stat' , methods=['GET', 'POST'])
def stat():
    print('autenticando')
    form = StatForm()
    print(form.validate_on_submit)
    if form.validate_on_submit():
        if current_user.is_authenticated:
            stat=Stat(id_usuario=current_user.id,dato_estadistico_1=request.form['estudios'], dato_estadistico_2=request.form['edad'], dato_estadistico_3=request.form['sexo'])
            print('autenticado')
    
        else:
            stat=Stat(dato_estadistico_1=request.form['estudios'], dato_estadistico_2=request.form['edad'], dato_estadistico_3=request.form['sexo'])
        stat.addStat()
        print('vaina2')

        return redirect(url_for('index'))
    return render_template('stat.html',title='stat', form=form)