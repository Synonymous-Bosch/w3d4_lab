from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import *

@app.route("/events")
def index():
    return render_template('index.html', title='Home', events=events)

@app.route("/events", methods=["POST"])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_location = request.form['room_location']
    event_number_of_guests = request.form['number_of_guests']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date, event_name, event_number_of_guests, event_location, event_description, event_recurring)
    add_new_event(new_event)
    return "Done"
