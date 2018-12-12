import os
from app import app
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root@35.230.143.0:3306/sis_inf_project_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
