from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql

app = Flask(__name__)
Bootstrap(app)

from config import Config

login = LoginManager(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)

from app import routes, models

db.create_all() # In case table doesn't exists already. Else remove it.    
db.session.commit()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
