# Manual Imports
from website.views.app import db
from website.models.relationships import slts, appnt

# External imports
from pytz import *

# Database imports
from flask_login import UserMixin


# --------------------------------------------- TABLES --------------------------------------------

class User(UserMixin, db.Model):
    id           =  db.Column(db.Integer,     primary_key=True,  nullable=False)
    firstname    =  db.Column(db.String(20),                     nullable=False)
    lastname     =  db.Column(db.String(20),                     nullable=False)
    username     =  db.Column(db.String(15),  unique=True,       nullable=False)
    email        =  db.Column(db.String(50),  unique=True,       nullable=False)
    password     =  db.Column(db.String(80),                     nullable=False)
    gender       =  db.Column(db.String(10),                     nullable=False)
    blood_group  =  db.Column(db.String(2),                      nullable=False)
    height_ft    =  db.Column(db.Integer,                        nullable=False)
    height_inch  =  db.Column(db.Integer,                        nullable=False)
    weight_kg    =  db.Column(db.Numeric,                        nullable=False)
    phone        =  db.Column(db.Numeric,     unique=True,       nullable=False)
    zipcode      =  db.Column(db.Numeric,                        nullable=False)
    city         =  db.Column(db.String(40),                     nullable=False)
    state        =  db.Column(db.String(40),                     nullable=False)

    appointments = db.relationship('Doctor', secondary=appnt, backref=db.backref('appointments', lazy='dynamic') )

    def __init__(self, id, firstname, lastname, username, email, password, gender, blood_group, height_ft, height_inch, weight_kg, phone, zipcode, city, state):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.blood_group = blood_group
        self.height_ft = height_ft
        self.height_inch = height_inch
        self.weight_kg = weight_kg
        self.phone = phone
        self.zipcode = zipcode
        self.city = city
        self.state = state

    def get_id(self):
        return (self.username)


class Doctor(UserMixin, db.Model):
    id           =  db.Column(db.Integer,     primary_key=True,  nullable=False)
    firstname    =  db.Column(db.String(20),                     nullable=False)
    lastname     =  db.Column(db.String(20),                     nullable=False)
    username     =  db.Column(db.String(15),  unique=True,       nullable=False)
    email        =  db.Column(db.String(50),  unique=True,       nullable=False)
    password     =  db.Column(db.String(80),                     nullable=False)
    gender       =  db.Column(db.String(10),                     nullable=False)
    blood_group  =  db.Column(db.String(2),                      nullable=False)
    height_ft    =  db.Column(db.Integer,                        nullable=False)
    height_inch  =  db.Column(db.Integer,                        nullable=False)
    weight_kg    =  db.Column(db.Numeric,                        nullable=False)
    type         =  db.Column(db.String(20),                     nullable=False)
    phone        =  db.Column(db.Numeric,     unique=True,       nullable=False)
    zipcode      =  db.Column(db.Numeric,                        nullable=False)
    city         =  db.Column(db.String(40),                     nullable=False)
    state        =  db.Column(db.String(40),                     nullable=False)

    slot = db.relationship('Slots', secondary=slts, backref=db.backref('slots', lazy='dynamic') )

    def __init__(self, id, firstname, lastname, username, email, password, gender, blood_group, height_ft, height_inch, weight_kg, type, phone, zipcode, city, state):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.blood_group = blood_group
        self.height_ft = height_ft
        self.height_inch = height_inch
        self.weight_kg = weight_kg
        self.type = type
        self.phone = phone
        self.zipcode = zipcode
        self.city = city
        self.state = state

    def get_id(self):
        return (self.username)


class Slots(db.Model):
    id            =  db.Column(db.Integer,  primary_key=True,  nullable=False)
    hour          =  db.Column(db.String,                      nullable=False)  # 10
    minute        =  db.Column(db.String,                      nullable=False)  # 3
    meridiem      =  db.Column(db.String,                      nullable=False)  # AM/PM
