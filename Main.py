# This is the Main File that loads all the other Modules

# Importing Required Modules

import datacoffee.User_Functions as User
import datacoffee.Other as Other
import datacoffee.Checks as Check
from time import sleep

# Initial  Checks

# Checking the connection to the MySQL Server
connection_status = Check.CheckConnection()
if connection_status is False:
    quit()
else:
    Check.CheckDatabase() # Checking for the Requirements of the Project
    Check.CreateTables() # Checking for the CreateTables of the Project

# Other.ClearScreen() #Clear the terminal Window

#Final Imports

# Ask for the Input and Process it


while True:
    Other.Menu()
    ans = input("Choose an Option Number: ")
    if ans == "1":
        User.OrderCoffee()
    elif ans == "2":
        User.CancelOrdering()
    elif ans == "3":
        User.ShowOrder()
    elif ans == "4":
        User.Datacoffee()
    elif ans == "5":
        Other.ClearScreen()
        Other.Menu()
    elif ans == "6":
        Other.Menu()
    elif ans == "7":
        Other.ClearScreen()
        Other.About()
        while True:
            ask = input("Do you want to Display Menu(Y/N): ")
            if ask in ["Y", "y"]:
                Other.Menu()
                break
            elif ask in ["N", "n"]:
                break
            else:
                print("Please Enter either Y (Yse) or N (No)!")
    elif ans == "8":
        print("Closing all Connection..")
        sleep(0.5)
        print("Thank You!")
        quit()
    else:
        print("Please Enter a Valid Option Number!")
 


