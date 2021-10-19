# Manual Imports
from website.views.app import db, app

# External imports
from pytz import *

# Form imports
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import *
from wtforms.validators import InputRequired, Length, Email
from wtforms.fields.html5 import EmailField, DecimalField

# Database imports
from flask_sqlalchemy import SQLAlchemy


state_choices = ['Andhra Pradesh', 'Andaman and Nicobar Islands', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
                 'Chhattisgarh', 'Dadar and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Lakshadweep', 'Puducherry',
                 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka',
                 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
                 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand',
                 'West Bengal']
blood_group_choices = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'NA']
height_ft_choices = [1, 2, 3, 4, 5, 6, 7, 8]
height_inch_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
doctor_type_choices = ['heart', 'ear', 'nose', 'tooth', 'throat', 'bones', 'veterinary', 'brain', 'lungs', 'radiologist']


# ---------------------------------------------- FORMS --------------------------------------------

class LoginForm(FlaskForm):
    username = StringField('Username : ', validators=[InputRequired(message='Username is required'), Length(min=4, max=40, message="User name must be 4 to 16 characters long !!!")])
    password = PasswordField('Password : ', validators=[InputRequired(message='Password is required'), Length(min=8, max=80, message="Password must be minimum 8 characters long !!!")])
    remember = BooleanField('Stay signed in')
    recaptcha = RecaptchaField()


class RegisterUserForm(FlaskForm):
    firstname = StringField('First name : ', validators=[InputRequired(message='First name is required'), Length(min=4, max=20, message="First name must be 4 to 20 characters long !!!")])
    lastname = StringField('Last name : ', validators=[InputRequired(message='Last name is required'), Length(min=4, max=20, message="Last name must be 4 to 20 characters long !!!")])
    username = StringField('Username : ', validators=[InputRequired(message='Username is required'), Length(min=4, max=16, message="User name must be 4 to 16 characters long !!!")])
    email = EmailField('Email : ', validators=[InputRequired(message='Email Address is required'), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password : ', validators=[InputRequired(message='Password is required'), Length(min=8, max=80, message="Password must be minimum 8 characters long !!!")])
    
    gender = SelectField('Gender : ', choices=['Male', 'Female', 'Other'], validators=[InputRequired(message='Your gender is required !!!')])
    blood_group = SelectField('Blood group : ', choices = blood_group_choices, default='O+', validators = [InputRequired(message='Blood group is required !!!')])
    height_ft = SelectField('Height (feet) : ', choices = height_ft_choices, default=5, validators = [InputRequired(message='Height is required !!!')])
    height_inch = SelectField('Height (inch) : ', choices = height_inch_choices, default=7, validators = [InputRequired(message='Height is required !!!')])
    weight_kg = DecimalField('Weight (kg) : ', validators = [InputRequired(message='Weight is required !!!')])
    
    phone = DecimalField('Phone Number : ', validators = [InputRequired(message='Phone number is required !!!')])
    zipcode = DecimalField('Zip code : ', validators = [InputRequired(message='Zipcode is required !!!')])
    city = StringField('City : ', validators=[InputRequired(message='City name is required')])
    state = SelectField('State : ', choices=state_choices, validators=[InputRequired(message='State name is required')])


class RegisterDoctorForm(FlaskForm):
    firstname = StringField('First name : ', validators=[InputRequired(message='First name is required'), Length(min=4, max=20, message="First name must be 4 to 20 characters long !!!")])
    lastname = StringField('Last name : ', validators=[InputRequired(message='Last name is required'), Length(min=4, max=20, message="Last name must be 4 to 20 characters long !!!")])
    username = StringField('Username : ', validators=[InputRequired(message='Username is required'), Length(min=4, max=16, message="User name must be 4 to 16 characters long !!!")])
    email = EmailField('Email : ', validators=[InputRequired(message='Email Address is required'), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password : ', validators=[InputRequired(message='Password is required'), Length(min=8, max=80, message="Password must be minimum 8 characters long !!!")])
    
    gender = SelectField('Gender : ', choices=['Male', 'Female', 'Other'], validators=[InputRequired(message='Your gender is required !!!')])
    blood_group = SelectField('Blood group : ', choices = blood_group_choices, default='O+', validators = [InputRequired(message='Blood group is required !!!')])
    height_ft = SelectField('Height (feet) : ', choices = height_ft_choices, default=5, validators = [InputRequired(message='Height is required !!!')])
    height_inch = SelectField('Height (inch) : ', choices = height_inch_choices, default=7, validators = [InputRequired(message='Height is required !!!')])
    weight_kg = DecimalField('Weight (kg) : ', validators = [InputRequired(message='Weight is required !!!')])
    
    type = SelectField('Select type : ', choices=doctor_type_choices, default='ear', validators = [InputRequired(message='Type is required !!!')])
    phone = DecimalField('Phone Number : ', validators = [InputRequired(message='Phone number is required !!!')])
    zipcode = DecimalField('Zip code : ', validators = [InputRequired(message='Zipcode is required !!!')])
    city = StringField('City : ', validators=[InputRequired(message='City name is required')])
    state = SelectField('State : ', choices=state_choices, validators=[InputRequired(message='State name is required')])


class Appointment(FlaskForm):
    date = StringField('Date : ')
    time = StringField('Time : ')


class AllSlots(FlaskForm):
    time = StringField('Time : ')
    # " ['08:00 AM', '09:30 AM'] "
