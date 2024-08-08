import calendar
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
import json

def load_entries():
    with open('/home/dci-student/Desktop/calendar_Leon/entries.json') as f:
        data = json.load(f) 
    return data['entries']

def save_entry(entries):
    with open('/home/dci-student/Desktop/calendar_Leon/entries.json','w') as file:
        json.dump({"entries":entries},file,indent=4)

def display_current_month():                                       
    print()
    print(calendar.month(year,month))

def display_current_year():                                        
    print()
    print(calendar.calendar(year))

def add_entry(data,type,name_or_description,date):
    if type == 'b':                                    
        data["birthdays"].update({name_or_description : date})               
    elif type == 'm':
        data["meetings"].update({name_or_description : date})
    elif type == 'e':
        data["events"].update({name_or_description : date})   
    save_entry(data)
    print("Entry saved!")                                                            

def get_entry(data,type,name_or_description):
    if type == 'b': 
        dict_birth = data["birthdays"]
        for key,value in dict_birth.items():
            if key == name_or_description:
                return key,value
        else:
            return 'No entry found.'
    if type == 'm':
        dict_meet = data["meetings"] 
        for key,value in dict_meet.items():
            if key == name_or_description:
                return key,value
        else:
            return 'No entry found.'
    if type == 'e': 
        dict_event = data["events"]
        for key,value in dict_event.items():
            if key == name_or_description:
                return key,value
        else:
            return 'No entry found.'

def display_entry(data,type,name_or_description):
    entry = get_entry(data,type,name_or_description)
    print(f'{name_or_description} : {entry[1]}')           
    
def delete_entry(data,type,name_or_description):
    entry = get_entry(data,type,name_or_description)
    if entry[0] in data["birthdays"]:
        del data["birthdays"][entry[0]]   
    elif entry[0] in data["meetings"]:
        del data["meetings"][entry[0]]
    elif entry[0] in data["events"]:
        del data["events"][entry[0]]
    save_entry(data)      
    print("Entry deleted!") 
    
def change_entry(data,type,name_or_description,new_date):
    entry = get_entry(data,type,name_or_description)  
    
    if entry[0] in data["birthdays"]:
        data["birthdays"].update({entry[0] : new_date})  
    elif entry[0] in data["meetings"]:
        data["meetings"].update({entry[0] : new_date})
    elif entry[0] in data["events"]:
        data["events"].update({entry[0] : new_date})   
    save_entry(data)      
    print("Entry successfully changed!")  
    
def show_all(data,type):
    if type == 'b': 
        print(data["birthdays"])
    elif type == 'm':
        print(data["meetings"])
    elif type == 'e':
        print(data["events"])
    
    