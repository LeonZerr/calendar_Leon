import calendar
import datetime
from calendar_functions import *


year = datetime.datetime.now().year
month = datetime.datetime.now().month

def main():
    while True:
        print("\n1. Show the current month.")
        print("2. Show the current year.")
        print("3. Add an event.")
        print("4. Add a birthday.")
        print("5. Change an event.")
        print("6. Delete an event.")
        print("7. Delete a birthday.")
        print("8. Show all events.")
        print("9. Show all birthdays.")
        print("10. Show birthday of a specific person.")
        print("11. Show specific event.")
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
