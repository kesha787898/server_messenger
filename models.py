from init import db
from datetime import datetime
from flask import jsonify

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), unique=False)
    category = db.Column(db.String(), unique=False)
    time = db.Column(db.DateTime(), unique=False)
    #from
    #to



    def __init__(self, text, category):
        self.text = text
        self.category = category
        self.category = datetime.now()
    def jsonify(self):
        return jsonify(id=self.id,
                       text=self.text,
                       category=self.category,
                       time=self.time
                       #,from=self.from,#to=self.to
                       )
