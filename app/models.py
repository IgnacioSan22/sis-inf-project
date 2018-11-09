from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Campos
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    tipo_usuario = Column(Integer)
    validated = Column(Integer)

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
    
    def validate(self):
        self.validated = True
        self.tipo_usuario = 2
        self.updateUser()

    def invalidate(self):
        self.validated = False
        self.updateUser()

    @classmethod
    def getUserByUsername(cls, username):
        return User.query.filter_by(username=username).first()
    
    @classmethod
    def getUserById(cls, id):
        return User.query.filter_by(id=id).first()
    
    @classmethod
    def getUsersNotValidated(cls):
        return User.query.filter_by(validated=0).all()

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
    titulo = Column(String(1024))
    reto = Column(String(2048))
    info = Column(String(2048))
    pregunta = Column(String(1024))
    respuesta_correcta = Column(Integer)
    corregido = Column(Integer)

    # Representación del poster
    def __repr__(self):
        return '<id: {}, id_usuario: {}, info: {}>'.format(self.id, self.id_usuario, self.info)

    #Interfaz
    def addPoster(self):
        db.session.add(self)
        db.session.commit()
    
    def removePoster(self):
        db.session.delete(self)
        db.session.commit()
    
    def validate(self):
        self.corregido = 1
        self.updatePoster()
    
    def denyPoster(self):
        self.corregido = 2
        self.updatePoster()

    def updatePoster(self):
        Poster.query.filter_by(id=self.id).update(dict(id_usuario=self.id_usuario, corregido=self.corregido, imagen=self.imagen, reto=self.reto, info=self.info, pregunta=self.pregunta, respuesta_correcta=self.respuesta_correcta))
        db.session.commit()

    @classmethod
    def getPosterById(cls, id):
        return Poster.query.filter_by(id=id).first()

    @classmethod
    def getPosterByUserId(cls, user_id):
        return Poster.query.filter_by(id_usuario=user_id).all()

    @classmethod
    def getPosters(cls):
        return Poster.query.all()

    @classmethod
    def getPostersNotChecked(cls):
        return Poster.query.filter_by(corregido=0).all()
    
    @classmethod
    def getPostersChecked(cls):
        return Poster.query.filter_by(corregido=1).all()

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
        QuestionOption.query.filter_by(id=self.id).update(dict(id_poster=self.id_poster, opcion=self.opcion))
        db.session.commit()

    @classmethod
    def getOpcionPreguntaByPosterId(cls, id_poster):
        return QuestionOption.query.filter_by(id_poster=id_poster).all()

class UserResponse(db.Model):
    __tablename__ = 'user_response'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    id_opcion = Column(Integer, ForeignKey('question_options.id'))

    # Reperesentación de UserResponse
    def __resp__(self):
        return '<id: {}, id_user: {}, id_opcion:{}>'.format(self.id, self.id_usuario, self.id_opcion)

    #Interfaz
    def addUserResponse(self):
        db.session.add(self)
        db.session.commit()
    
    def removeUserResponse(self):
        db.session.delete(self)
        db.session.commit()

    def updateUserResponse(self):
        UserResponse.query.filter_by(id=self.id).update(dict(id_user=self.id_usuario, id_opcion=self.id_opcion))
        db.session.commit()

    @classmethod
    def getUserResponseByUserId(cls, id_usuario):
        return UserResponse.query.filter_by(id_usuario=id_usuario).all()

class UserLike(db.Model):
    __tablename__ = 'user_likes'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    id_poster = Column(Integer, ForeignKey('posters.id'))

    #Interfaz
    def likePoster(self):
        db.session.add(self)
        db.session.commit()

    def unlikePoster(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def getUserLikes(cls, id_usuario):
        return UserLike.query.filter_by(id_usuario=id_usuario).all()

    @classmethod
    def getPosterLikes(cls, id_poster):
        return UserLike.query.filter_by(id_poster=id_poster).count()
    
    @classmethod
    def gaveLike(cls, id_usuario, id_poster):
        return UserLike.query.filter_by(id_usuario=id_usuario, id_poster=id_poster).first() is not None