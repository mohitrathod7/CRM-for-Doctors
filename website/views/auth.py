# Manual imports
from website.models.forms import RegisterUserForm, RegisterDoctorForm, LoginForm
from website.models.tables import User, Doctor
from website.views.app import login_manager, db

# Flask imports
from flask import Blueprint, render_template, redirect, url_for, request, flash, session

# Form imports
from wtforms import *
from wtforms.validators import *

# Database imports
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/signup/')
def sign_up():
    return redirect(url_for('auth.sign_up_as_user'))


@auth.route('/signup/user/', methods=["POST", "GET"])
def sign_up_as_user():
    form = RegisterUserForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        
        # Count no of rows (users) to get current ID
        total_id = User.query.filter(User.id > 0).count()
        
        id = total_id + 1
        firstname = form.firstname.data.lower().capitalize()
        lastname = form.lastname.data.lower().capitalize()
        username = form.username.data.lower()
        email = form.email.data.lower()
        password = hashed_password
        gender = form.gender.data.lower().capitalize()
        blood_group = form.blood_group.data.capitalize()
        height_ft = form.height_ft.data
        height_inch = form.height_inch.data
        weight_kg = form.weight_kg.data
        phone = form.phone.data
        zipcode = form.zipcode.data
        city = form.city.data.lower().capitalize()
        state = form.state.data.lower().capitalize()

        new_user = User(id, firstname, lastname, username, email, password, gender, blood_group, height_ft, height_inch, weight_kg, phone, zipcode, city, state)
        
        status = ""

        try:
            db.session.add(new_user)
            status = "success"
        except:
            db.session.rollback()
            status = "error"
        finally:
            db.session.commit()

            if status == "success":
                flash("Successfully Signed up", "success")
                return redirect(url_for('auth.log_in'))
            else:
                flash("Signing up failed", "error")
                return render_template("pages/auth/signupUser.html", form=form)
    else:
        return render_template("pages/auth/signupUser.html", form=form)   
        

@auth.route('/signup/doctor/', methods=["POST", "GET"])
def sign_up_as_doctor():
    form = RegisterDoctorForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        
        # Count no of rows (doctors) to get current ID
        total_id = Doctor.query.filter(Doctor.id > 0).count()
        
        id = total_id + 1
        firstname = form.firstname.data.lower().capitalize()
        lastname = form.lastname.data.lower().capitalize()
        username = form.username.data.lower()
        email = form.email.data.lower()
        password = hashed_password
        gender = form.gender.data.lower().capitalize()
        blood_group = form.blood_group.data.capitalize()
        height_ft = form.height_ft.data
        height_inch = form.height_inch.data
        weight_kg = form.weight_kg.data
        type = form.type.data.lower().capitalize()
        phone = form.phone.data
        zipcode = form.zipcode.data
        city = form.city.data.lower().capitalize()
        state = form.state.data.lower().capitalize()

        new_doctor = Doctor(id, firstname, lastname, username, email, password, gender, blood_group, height_ft, height_inch, weight_kg, type, phone, zipcode, city, state)

        status = ""

        try:
            db.session.add(new_doctor)
            status = "success"
        except:
            db.session.rollback()
            status = "error"
        finally:
            db.session.commit()

            if status == "success":
                flash("Successfully Signed up", "success")
                return redirect(url_for('auth.log_in'))
            else:
                flash("Signing up failed", "error")
                return render_template("pages/auth/signupDoctor.html", form=form)
    else:
        return render_template("pages/auth/signupDoctor.html", form=form)   
  

@auth.route("/login/", methods=["POST", "GET"])
def log_in():
    form = LoginForm()

    if form.validate_on_submit():
        next_url = request.form.get("next")

        for i in ['user', 'doctor']:
            for j in ['username', 'email']:
                try:
                    if i == 'user':
                        if j == 'username':
                            person = User.query.filter_by(username=form.username.data.lower()).first()
                        elif j == 'email':
                            person = User.query.filter_by(email=form.username.data.lower()).first()
                        
                    elif i == 'doctor':
                        if j == 'username':
                            person = Doctor.query.filter_by(username=form.username.data.lower()).first()
                        elif j == 'email':
                            person = Doctor.query.filter_by(email=form.username.data.lower()).first()
                        
                    if check_password_hash(person.password, form.password.data):
                        login_user(person, remember=form.remember.data)
                        db.session.commit()

                        session["id"] = str(current_user.id)
                        session["username"] = str(current_user.username)

                        if next_url:
                            flash("Successfully Logged in ", "success")
                            return redirect(next_url)
                        else:
                            flash("Successfully Logged in ", "success")
                            return redirect(url_for('home.homepage'))
                    else:
                        flash("The username or password is incorrect", "error")
                        return render_template("pages/auth/login.html", form=form)
                except:
                    pass
        flash("This Username or Email ID doesn't exist", "error")

    return render_template("pages/auth/login.html", form=form)
    

@auth.route("/logout/")
@login_required
def log_out():
    db.session.commit()
    logout_user()

    session["id"] = None
    session["username"] = None

    flash("Successfully Logged out", "success")
    return redirect(url_for('home.homepage'))


@login_manager.user_loader
def load_user(username):
    person = User.query.filter_by(username=username).first()

    # checking does given username/email exist in User table
    if person is not None: 
        return ( User.query.get(person.id) )
    # checking does given username/email exist in Doctor table
    else:
        person = Doctor.query.filter_by(username=username).first()
        return ( Doctor.query.get(person.id) )
    # pass