from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tipo = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Respuestas(db.Model):
    id_respuesta = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, index=True, unique=True)
    p1 = db.Column(db.String(64))
    p2 = db.Column(db.String(64))

class Carteles(db.Model):
    id_cartel = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, index=True)
    img = db.Column(db.String(1024))
    reto = db.Column(db.String(1024))
    info = db.Column(db.String(1024))
    pregunta = db.Column(db.String(1024))
    correcta = db.Column(db.Integer)

class OpcionesPregunta(db.Model):
    id_cartel = db.Column(db.Integer, primary_key=True, index=True)
    opcion = db.Column(db.String(512))

