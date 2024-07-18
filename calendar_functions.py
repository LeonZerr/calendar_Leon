import calendar
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month

def display_current_month():
    print()
    print(calendar.month(year,month))

def display_current_year():
    print()
    print(calendar.calendar(year))

def add_an_event(datetime,description):
       datetime = input()
    
    