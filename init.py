from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://sbnznvbc:hp8MJlywM0NsnCje68RgDst6ssQs8Hd5@balarama.db.elephantsql.com:5432/sbnznvbc'

db =SQLAlchemy(app)

