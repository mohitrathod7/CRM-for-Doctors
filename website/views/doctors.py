# Inbuilt imports
import calendar, datetime, math

# External imports
from pytz import *

# Flask imports
from flask import Blueprint, render_template, session, redirect

# Manual imports
from website.models.tables import Doctor, User
from website.models.forms import Appointment

# Database imports
from flask_login import login_required


doctors = Blueprint('doctors', __name__)


# For doctor profile ------------------------------------------------------------------------------

@doctors.route('/categories/<doctor_type>/')
def doctor_profile_by_type(doctor_type):
    doctors = Doctor.query.filter_by(type=doctor_type.capitalize()).all()

    message = "No doctors found for " + doctor_type + " !"
    if doctor_type == "radiologist":
        message = "No " + doctor_type + " found !"

    if doctors:
        return render_template("pages/home.html", doctors=doctors)
    else:
        return render_template("pages/home.html", message=message)


@doctors.route('/<doctor_id>/')
def doctor_profile(doctor_id):
    doctors = Doctor.query.filter_by(id=doctor_id).first()

    if doctors:
        return render_template("pages/doctor/doctorProfile.html", doctors=doctors)
    else:
        return "<h1>Doctor not found !!!</h1>"


# For appointments --------------------------------------------------------------------------------

@doctors.route('/<doctor_id>/appointment/booking/')
@login_required
def doctor_appointment(doctor_id):
    form = Appointment()
    
    # Current time in UTC
    today_utc = datetime.datetime.now(timezone('UTC'))
    
    # Convert to Asia/Kolkata time zone
    today_india = today_utc.astimezone(timezone('Asia/Kolkata'))

    # Date variables
    date         =  int(today_india.strftime("%d"))     # 7
    hour         =  int(today_india.strftime("%I"))     # 07
    minute       =  int(today_india.strftime("%M"))     # 7
    meridiem     =  today_india.strftime("%p")          # AM
    weekday      =  today_india.strftime("%a")          # SUN
    weekday_int  =  today_india.strftime("%u")          # 1
    month        =  today_india.strftime("%b")          # APR
    month_int    =  today_india.strftime("%m")          # 4
    year_full    =  today_india.strftime("%Y")          # 2021
    year_short   =  today_india.strftime("%y")          # 21

    dates = []
    slots = {}
    no_of_days = 3     # Number of days to take appointment in future

    for i in range(0, no_of_days):
        loop_date = today_india + datetime.timedelta(days=i)
        date = {}
        date["weekday"] = loop_date.strftime("%a")
        date["date"] = loop_date.strftime("%d")
        date["month"] = loop_date.strftime("%b")
        date["month_int"] = loop_date.strftime("%m")
        date["year_full"] = loop_date.strftime("%Y")

        dates.append(date)

    # Above loop is used to create alike this list of future days for appointment
    # dates = [   {'weekday': 'Tue', 'date': '12', 'month': 'Mar', 'month_int': 3, 'year_full': 2021},
    #             {'weekday': 'Wed', 'date': '13', 'month': 'Mar', 'month_int': 3, 'year_full': 2021}
    #         ]
    
    for i in range(0, no_of_days):
        loop_date = today_india + datetime.timedelta(days=i)
        slot = {}
        slot["hour"] = loop_date.strftime("%a")
        slot["minute"] = loop_date.strftime("%a")
        slot["meridiem"] = loop_date.strftime("%a")
        slot["date"] = loop_date.strftime("%d")
        slot["month_int"] = loop_date.strftime("%m")
        slot["year_full"] = loop_date.strftime("%Y")

        # slots.append(date)
    # get json list of all slots from database column and using loop print all available slots
    # 
    # slots = {  "date-month_int-year_full": [ ['hour', 'minute', 'meridiem'],
    #                                          ['hour', 'minute', 'meridiem']
    #                                        ],
    # 
    #            "13-10-2021": [ ['12', 3, 'AM'],
    #                            ['12', 3, 'PM']
    #                          ]
    #         }
    
    return render_template("pages/doctor/doctorAppointment.html", form=form, dates=dates, _doctor_id=doctor_id)


@doctors.route('/<doctor_id>/appointment/confirmation/')
def doctor_appointment_confirmation(doctor_id):
    form = ""
    return render_template("pages/doctor/appointmentConfirmation.html", form=form)


# For ratings -------------------------------------------------------------------------------------

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def fetch_rating():
    _5_stars_count = 252
    _4_stars_count = 124
    _3_stars_count = 40
    _2_stars_count = 29
    _1_stars_count = 33

    _5_stars_sum = 5 * _5_stars_count
    _4_stars_sum = 4 * _4_stars_count
    _3_stars_sum = 3 * _3_stars_count
    _2_stars_sum = 2 * _2_stars_count
    _1_stars_sum = 1 * _1_stars_count

    total_rating = _5_stars_sum + _4_stars_sum + _3_stars_sum + _2_stars_sum + _1_stars_sum
    total_count = _5_stars_count + _4_stars_count + _3_stars_count + _2_stars_count + _1_stars_count
    
    overall_rating = round_up( (total_rating / total_count), decimals=3 )
