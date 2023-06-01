from models.event import *
import datetime

event1 = Event(datetime.date(2023, 6, 12), "Quickening", 20, "Gallery of Modern Art", "There can be only one!", True)
event2 = Event(datetime.date(2024, 5, 15), "Wedding", 50, "Killearn Church", "A ritual shackling of souls and formalisation of chore list", False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)