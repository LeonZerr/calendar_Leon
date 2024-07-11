import calendar
import datetime
from calendar_functions import *

year = datetime.datetime.now().year
month = datetime.datetime.now().month

def main():
    while True:
        print("\n1. Show current month")
        print("2. Show current year")
        print("3. Add event/birthday")
        print("4. Change event")
        print("5. Delete event")
        print("6. Show all events")
        print("7. Show all birthdays")
        #print("8. Show events for a specific month")
        #print("9. Show birthdays for a specific month")
        print("q. Exit")
        
        option = input("\nSelect an option: ")
        if option == '1':
          display_current_month()
        elif option == '2':
          display_current_year()  
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")    
main() 