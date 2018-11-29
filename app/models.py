from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text, func
from  sqlalchemy.sql.expression import func, select

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Campos
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    nombre = Column(String(64))
    apellidos = Column(String(64))
    nia = Column(String(6), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    tipo_usuario = Column(Integer)
    validated = Column(Integer)

    # Representación del Usuario
    def __repr__(self):
        return '<ID: {}, NIA: {}, email: {}>'.format(self.id, self.nia, self.email)

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
    id_usuario = Column(Integer, unique=True)
    dato_estadistico_1 = Column(String(64))
    dato_estadistico_2 = Column(String(64))
    dato_estadistico_3 = Column(String(64))

    # Representación del dato estadístico
    def __repr__(self):
        return '<id: {}, id_usuario: {}, dato_estadistico_1: {}, datos_estadistico_2: {}, datos_estadistico_3>'.format(self.id, self.id_usuario, self.dato_estadistico_1, self.dato_estadistico_2, self.dato_estadistic_3)

    #Interfaz
    def addStat(self):
        db.session.add(self)
        db.session.commit()
    
    def removeStat(self):
        db.session.delete(self)
        db.session.commit()

    def updateStat(self):
        Stat.query.filter_by(id=self.id).update(dict(dato_estadistico_1=self.dato_estadistico_1, dato_estadistico_2=self.dato_estadistico_2, dato_estadistic_3=self.dato_estadistic_3))
        db.session.commit()
    
    @classmethod
    def getStatById(cls, id):
        return Stat.query.filter_by(id=id).first()

    @classmethod
    def getUsers(cls,id):
        return Stat.query.filter_by(id_usuario=id).first()
    @classmethod
    def getCountByDE1(cls, filter):
        return Stat.query.filter_by(dato_estadistico_1=filter).count()

    @classmethod
    def getCountByDE2(cls, filter):
        return Stat.query.filter_by(dato_estadistico_2=filter).count()

    @classmethod
    def getCountByDE3(cls, filter):
        return Stat.query.filter_by(dato_estadistico_3=filter).count()

#######################################################
#######################################################

class Pregunta(db.Model):
    __tablename__ = 'preguntas'

    id = Column(Integer, primary_key=True)
    pregunta = Column(String(1024))
    year = Column(Integer)

    def addPregunta(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getRandomQuestions(cls):
        return db.session.query(Pregunta).order_by(func.rand()).all()
    
    @classmethod
    def getNext(cls,num):
        preg=Pregunta.query.all()
        return preg[num]
    
    @classmethod
    def numPreg(cls):
        return len(Pregunta.query.all())
    

class QuestionOption2(db.Model):
    __tablename__ = 'question_options_2'
    
    id = Column(Integer, primary_key=True)
    id_pregunta = Column(Integer, ForeignKey('preguntas.id'))
    opcion = Column(String(512))
    correcta = Column(Integer)

    # Reperesentación de QuestionOption
    def __resp__(self):
        return '<id: {}, id_poster: {}, opcion:{}>'.format(self.id, self.id_pregunta, self.opcion)

    @classmethod
    def newOption(cls, pregunta_id, respuesta, es_correcta):
        if respuesta != "":
            resp = QuestionOption2(id_pregunta=pregunta_id,opcion=respuesta,correcta=es_correcta)
            db.session.add(resp)
            db.session.commit()

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
    def getOpcionPreguntaByPreguntaId(cls, id_pregunta):
        return QuestionOption2.query.filter_by(id_pregunta=id_pregunta).all()

    @classmethod
    def checkAnswer(cls,opciones_dadas,pregunta):
        options = QuestionOption2.getOpcionPreguntaByPreguntaId(pregunta)
        print(opciones_dadas)
        for i in range (0,len(options)):
            if options[0].correcta!=opciones_dadas[0]:
                return False
        return True


class UserResponse2(db.Model):
    __tablename__ = 'user_response2'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    id_opcion = Column(Integer, ForeignKey('question_options_2.id'))

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

#######################################################
#######################################################

class Poster(db.Model):
    __tablename__ = 'posters'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    imagen = Column(String(1024))
    titulo = Column(String(1024))
    reto = Column(Text(8192))
    info = Column(Text(16384))
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
    id_poster = Column(Integer)
    opcion = Column(String(512))
    correcta = Column(Boolean)

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
    id_poster = Column(Integer)
    opcion = Column(String(100))

    # Reperesentación de UserResponse
    def __resp__(self):
        return '<id: {}, id_user: {}, id_poster:{}, opcion:{}>'.format(self.id, self.id_usuario, self.id_poster,self.opcion)

    #Interfaz
    def addUserResponse(self):
        db.session.add(self)
        db.session.commit()
    
    def removeUserResponse(self):
        db.session.delete(self)
        db.session.commit()

    def updateUserResponse(self):
        UserResponse.query.filter_by(id=self.id).update(dict(id_user=self.id_usuario, id_poster=self.id_poster, opcion =self.opcion))
        db.session.commit()

    @classmethod
    def getUserResponseByUserId(cls, id_usuario):
        return UserResponse.query.filter_by(id_usuario=id_usuario).all()

class UserLike(db.Model):
    __tablename__ = 'user_likes'

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    id_poster = Column(Integer)

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