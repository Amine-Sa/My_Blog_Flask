from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ee24808950fd24f818ba6ee3763d29c' #secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
db = SQLAlchemy(app)

from My_Blog_Flask import routes