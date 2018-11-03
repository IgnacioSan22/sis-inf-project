from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data, validated=1).first()
        if user is None:
            raise ValidationError('Usuario no validado por un administrador.')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PosterForm(FlaskForm):
    imagen = StringField('URL Imagen', validators=[DataRequired()])
    titulo = StringField('Título', validators=[DataRequired()])
    reto = StringField('Reto', validators=[DataRequired()])
    info =  StringField('Información', validators=[DataRequired()])
    pregunta = StringField('Pregunta', validators=[DataRequired()])
    respuesta1 = StringField('Respuesta 1', validators=[DataRequired()])
    respuesta2 = StringField('Respuesta 2', validators=[DataRequired()])
    respuesta3 = StringField('Respuesta 3', validators=[DataRequired()])
    respuesta4 = StringField('Respuesta 4', validators=[DataRequired()])
    submit = SubmitField('Upload')

class ValidateUserForm(FlaskForm):
    user = HiddenField('')
    action = HiddenField('')
    validate = SubmitField('Validar')
    deny = SubmitField('Denegar')

class ValidatePosterForm(FlaskForm):
    id = HiddenField('')
    action = HiddenField('')
    validate = SubmitField('Validar')
    deny = SubmitField('Denegar')