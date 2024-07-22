import calendar
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
import json

def load_events():
    with open('events.json') as f:
        data = json.load(f) 
    return data['events']

def save_events(events):
    with open('events.json','w') as file:
        json.dump({"events":events},file,indent=4)



    
def display_current_month():
    print()
    print(calendar.month(year,month))

def display_current_year():
    print()
    print(calendar.calendar(year))

def add_an_event(datetime,description):
       datetime = input()
    
    