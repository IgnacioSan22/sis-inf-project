from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, RadioField, SelectMultipleField
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
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class ValidateUserForm(FlaskForm):
    user = HiddenField('')
    action = HiddenField('')
    validate = SubmitField('Validar')
    deny = SubmitField('Denegar')

class ValidatePosterForm(FlaskForm):
    validate = SubmitField('Validar')
    deny = SubmitField('Denegar')

class StatForm(FlaskForm):
    estudios = RadioField('Estudios', choices=[('Universitarios', 'menor'), ('Bachiller', 'mayor'), ('Acabados','muy mayor')])
    edad = RadioField ('Edad', choices=[('0-18','menor'), ('18-22','mayor'), ('+22', 'muy mayor')])
    submit = SubmitField('Enviar')



