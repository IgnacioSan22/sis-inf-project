from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_login import LoginManager
import pymysql

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/sis-inf-project-db'
login = LoginManager(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
#migrate = Migrate(app, db)
login = LoginManager(app)
#login.login_view = 'login'

from app import routes, models

db.create_all() # In case user table doesn't exists already. Else remove it.    
db.session.commit() # This is needed to write the changes to database