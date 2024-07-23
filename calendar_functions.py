import calendar
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
import json

def load_entries():
    with open('entries.json') as f:
        data = json.load(f) 
    return data['entries']

def save_entries(entries):
    with open('entries.json','w') as file:
        json.dump({"entries":entries},file,indent=4)

def display_current_month():
    print()
    print(calendar.month(year,month))

def display_current_year():
    print()
    print(calendar.calendar(year))

def add_entry(type,name_or_description,date):
    if type == 'birthday':
        entries.birthday.append("name_or_description":name_or_description,"date":date)
    elif type == 'meeting':
        entries.meeting.append("name_or_description":name_or_description,"date":date)
    elif type == 'event':
        entries.event.append("name_or_description":name_or_description,"date":date)       
    save_entries(entries)

    
    