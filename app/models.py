from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, ForeignKey

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Campos
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    tipo_usuario = Column(Integer)

    # Representación del Usuario
    def __repr__(self):
        return '<ID: {}, User: {}, email: {}>'.format(self.id, self.username, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Interfaz
    def addUser(self):
        db.session.add(self)
        db.session.commit()
    
    def removeUser(self):
        db.session.delete(self)
        db.session.commit()

    def updateUser(self):
        User.query.filter_by(id=self.id).update(dict(username=self.username, email=self.email, password_hash=self.password_hash, tipo_usuario=self.tipo_usuario))
        db.session.commit()

    @classmethod
    def getUserByUsername(cls, username):
        return User.query.filter_by(username=username).first()
    
    @classmethod
    def getUserById(cls, id):
        return User.query.filter_by(id=id).first()

class Stat(db.Model):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'), unique=True)
    dato_estadistico_1 = Column(String(64))
    dato_estadistico_2 = Column(String(64))

    # Representación del dato estadístico
    def __repr__(self):
        return '<id: {}, id_usuario: {}, dato_estadistico_1: {}, datos_estadistico_2: {}>'.format(self.id, self.id_usuario, self.dato_estadistico_1, self.dato_estadistico_2)

    #Interfaz
    def addStat(self):
        db.session.add(self)
        db.session.commit()
    
    def removeStat(self):
        db.session.delete(self)
        db.session.commit()

    def updateStat(self):
        Stat.query.filter_by(id=self.id).update(dict(dato_estadistico_1=self.dato_estadistico_1, dato_estadistico_2=self.dato_estadistico_2))
        db.session.commit()
    
    @classmethod
    def getStatById(cls, id):
        return Stat.query.filter_by(id=id).first()

class Poster(db.Model):
    __tablename__ = 'posters'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    imagen = Column(String(1024))
    reto = Column(String(1024))
    info = Column(String(1024))
    pregunta = Column(String(1024))
    respuesta_correcta = Column(Integer, ForeignKey('question_options.id'))

    # Representación del poster
    def __repr__(self):
        return '<id: {}, id_usuario: {}>'.format(self.id, self.id_usuario)

    #Interfaz
    def addCartel(self):
        db.session.add(self)
        db.session.commit()
    
    def removeCartel(self):
        db.session.add(self)
        db.session.commit()

    def updateCartel(self):
        Poster.query.filter_by(id=self.id).update(dict(id_usuario=self.id_usuario, imagen=self.imagen, reto=self.reto, info=self.info, pregunta=self.pregunta, respuesta_correcta=self.respuesta_correcta))
        db.session.commit()

    @classmethod
    def getPosterById(cls, id):
        return Poster.query.filter_by(id=id).first()

class QuestionOption(db.Model):
    __tablename__ = 'question_options'
    
    id = Column(Integer, primary_key=True)
    id_poster = Column(Integer, ForeignKey('posters.id'))
    opcion = Column(String(512))

    # Reperesentación de QuestionOption
    def __resp__(self):
        return '<id: {}, id_poster: {}, opcion:{}>'.format(self.id, self.id_poster, self.opcion)

    #Interfaz
    def addOpcionPregunta(self):
        db.session.add(self)
        db.session.commit()
    
    def removeOpcionPregunta(self):
        db.session.delete(self)
        db.session.commit()

    def updateOpcionPregunta(self):
        Poster.query.filter_by(id=self.id).update(dict(id_poster=self.id_poster, opcion=self.opcion))
        db.session.commit()

    @classmethod
    def getOptionsByPosterId(cls, id_poster):
        return QuestionOption.query.filter_by(id_poster=id_poster).all()
