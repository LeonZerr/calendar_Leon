import calendar
import datetime
from calendar_functions import *

year = datetime.datetime.now().year
month = datetime.datetime.now().month
data = load_entries()

def main():
    while True:
        print("\n1. Show the current month.")
        print("2. Show the current year.")
        print("3. Add entry.")
        print("4. Show specific entry.")
        print("5. Delete entry.")
        print("6. Change entry.")
        print("7. Show all birthdays.")
        print("8. Show all events.")
        print("9. Show all meetings.")
        print("q. Exit")
        
        option = input("\nSelect an option: ")
        if option == '1':
          display_current_month()
        elif option == '2':
          display_current_year()  
        elif option == '3':
          type = input('Choose type(B = birthday, E = event or M = meeting): ')
          name_or_description = input('Enter the name(if birthday) or description(for an event or meeting): ')
          date = (input('Enter the date: '))
          add_entry(data,type,name_or_description,date)   
        elif option == '4':
          type = input('Choose type of entry you are searching for(B = birthday, E = event or M = meeting): ')
          name_or_description = (input('Enter the name/description of the entry: '))
          display_entry(data,type,name_or_description)
        
        
        
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")    
main() 
