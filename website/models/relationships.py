# Manual Imports
from website.views.app import db

# External imports
from pytz import *


# -------------------------------------- RELATIONSHIP TABLES --------------------------------------

# Appointment relationship table between users and doctors
appnt = db.Table('appnt',
            db.Column('user_id',      db.Integer,     db.ForeignKey('user.id'),    nullable=False),
            db.Column('doctor_id',    db.Integer,     db.ForeignKey('doctor.id'),  nullable=False),
            db.Column('date',         db.DateTime,                                 nullable=False),
            db.Column('time',         db.DateTime,                                 nullable=False),
            db.Column('status',       db.String(15),                               nullable=False)  # Status : (Pending, Completed)
        )


# Slots relationship table between doctors and slots
slts = db.Table('slts',
            db.Column('slot_id',    db.Integer,     db.ForeignKey('slots.id'),   nullable=False),
            db.Column('doctor_id',  db.Integer,     db.ForeignKey('doctor.id'),  nullable=False),
            db.Column('time',       db.String,      default="00:00:AM",          nullable=False),
            db.Column('status',     db.String(15),  default="active",            nullable=False)
        )
