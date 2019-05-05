from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import pickle

ma = Marshmallow()
db = SQLAlchemy()

current_dir = os.path.dirname(__file__)
clf = pickle.load(
    open(
        os.path.join(current_dir, 'pkl_objects', 'classifier.pkl'),
        'rb'
    )
)


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)
    posted_by = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, title, body, posted_by):
        self.title = title
        self.body = body
        self.posted_by = posted_by if posted_by else 'Anonymous'


class Passenger(db.Model):
    __tablename__ = 'passengers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    pclass = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Float(), nullable=False)
    sex = db.Column(db.Integer, nullable=False) # 'female': 0, 'male': 1
    fare = db.Column(db.Float(), nullable=False)
    family_size = db.Column(db.Integer, nullable=False)
    embarked = db.Column(db.Integer, nullable=False) # 0:S = Southampton; 1:C = Cherbourg; 2:Q = Queenstown;
    survived = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, first_name, last_name, pclass, age, sex, fare, family_size, embarked):
        self.first_name = first_name
        self.last_name = last_name
        self.pclass = pclass
        self.age = age
        self.sex = sex
        self.fare = fare
        self.family_size = family_size
        self.embarked = embarked
        self.survived = self.predict_survival()

    def predict_survival(self):
        feature_nparray = self.convert_to_nparray()
        result_nparray = clf.predict(feature_nparray)
        return int(result_nparray[0])

    def convert_to_nparray(self):
        return [
            [
                self.pclass,
                self.age,
                self.sex,
                self.fare,
                self.family_size,
                self.embarked
            ]
        ]


class EntrySchema(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    body = fields.String(required=True)
    posted_by = fields.String(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class PassengerSchema(ma.Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    pclass = fields.Integer(required=True)
    age = fields.Float(required=True)
    sex = fields.Integer(required=True)
    fare = fields.Float(required=True)
    family_size = fields.Integer(required=True)
    embarked = fields.Integer(required=True)
    survived = fields.Integer(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
