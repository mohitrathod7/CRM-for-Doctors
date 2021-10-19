# Manual imports
from website.views.app import db
from website.models.tables import User, Doctor, Slots

# Database imports
from werkzeug.security import generate_password_hash

# Inbuilt imports
import datetime


db.create_all()

hashed_password = generate_password_hash('123456789', method='sha256')

u = User(id=1, firstname='Mohit', lastname='Rathod', username='user1', email='u1@gmail.com', password=hashed_password, 
         gender='Male', blood_group='O+', height_ft=5, height_inch=7, weight_kg='50', phone='7977980818', zipcode='401101',
         city='Mumbai', state='Maharashtra')
db.session.add(u)

d = Doctor(id=1, firstname='Mohit', lastname='Rathod', username='doc1', email='d1@gmail.com', password=hashed_password,
           gender='Male', type="Ear", blood_group='O+', height_ft=5, height_inch=7, weight_kg='50', phone='7977980820',
           zipcode='401101', city='Mumbai', state='Maharashtra')
db.session.add(d)
 
# Add doctors' slots to Slots table
h = datetime.datetime.strptime('09:30:AM', "%H:%M:%p").hour
m = datetime.datetime.strptime('09:30:AM', "%H:%M:%p").minute
p = datetime.datetime.strptime('09:30:AM', "%H:%M:%p").strftime("%p")

doctor = Doctor.query.filter_by(id=1).first()

slot_timings = [ ['09', '00', 'AM'], ['09', '30', 'AM'], ['10', '00', 'AM'], ['10', '30', 'AM'], ['11', '00', 'AM'], ['11', '30', 'AM'],
                 ['12', '00', 'PM'], ['12', '30', 'PM'], ['01', '00', 'PM'], ['01', '30', 'PM'], ['02', '00', 'PM'], ['02', '30', 'AM'],
                 ['03', '00', 'PM'], ['03', '30', 'PM'], ['04', '00', 'PM'], ['04', '30', 'PM'], ['05', '00', 'PM'], ['05', '30', 'PM'],
                 ['06', '00', 'PM'], ['06', '30', 'PM'], ['07', '00', 'AM'], ['07', '30', 'PM'], ['08', '00', 'PM'], ['08', '30', 'PM']
               ]

for time in slot_timings:
    s = Slots( id=((slot_timings.index(time))+1), hour=time[0], minute=time[1], meridiem=time[2] )
    doctor.slot.append(s)
    db.session.commit()
