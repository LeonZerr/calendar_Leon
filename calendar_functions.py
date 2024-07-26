import calendar
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
import json

def load_entries():
    with open('/home/dci-student/Desktop/Python_projects/calendar_Leon/entries.json') as f:
        data = json.load(f) 
    return data['entries']

def save_entry(entries):
    with open('/home/dci-student/Desktop/Python_projects/calendar_Leon/entries.json','w') as file:
        json.dump({"entries":entries},file,indent=4)
        print("Entry saved!")

def display_current_month():                                       
    print()
    print(calendar.month(year,month))

def display_current_year():                                        
    print()
    print(calendar.calendar(year))

def add_entry(data,type,name_or_description,date):
    if type == 'B':                                    
        data["birthdays"].update({name_or_description : date})               
    elif type == 'M':
        data["meetings"].update({name_or_description : date})
    elif type == 'E':
        data["events"].update({name_or_description : date})   
    save_entry(data)                                                            

def get_entry(data,type,name_or_description):
    if type == 'B': 
        dict_birth = data["birthdays"]
        if name_or_description in dict_birth:
            return dict_birth[name_or_description]
        else:
            return 'No entry found.'
    if type == 'M':
        dict_meet = data["meetings"] 
        if name_or_description in dict_meet:
            return dict_meet[name_or_description]
        else:
            return 'No entry found.'
    if type == 'E': 
        dict_event = data["events"]
        if name_or_description in dict_event:
            return dict_event[name_or_description]
        else:
            return 'No entry found.'

def display_entry(data,type,name_or_description):
    entry = get_entry(data,type,name_or_description)
    print(f'{name_or_description} : {entry}')
    
    