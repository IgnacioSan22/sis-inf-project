import os
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_INFO') or 'mysql+pymysql://root@localhost:3306/sis-inf-project-db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False