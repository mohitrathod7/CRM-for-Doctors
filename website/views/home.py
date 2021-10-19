from flask import Blueprint, render_template
from website.models.tables import Doctor


home = Blueprint('home', __name__)

@home.route('/')
def homepage():
    doctors = Doctor.query.all()
    
    return render_template("pages/home.html", doctors=doctors)
