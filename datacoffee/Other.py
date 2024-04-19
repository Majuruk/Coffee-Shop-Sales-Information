# This Module has some Oter Commonly used Functions

# Importing Required Modules

import os
import time


# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameter -> None
    """
    # Change the path given here to the absolute path of the README file
    with open("Dataset/coffee_shop_sales.csv") as file:
        data = file.read()
        print(data)

    
def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameter -> None
    """

    print("Clearing..")
    time.sleep(2)
    os.system("cls")


def Menu(answer="Yes"):
    """
    Menu() -> Display the Menu

    Parameter -> Answer (User's choice on Displaying the Menu, by default it is set to True)
    """

    if answer in ["Yes", "Y"]:
        print("  Welcome To Coffee Shop Information")
        print("1. Order coffee")
        print("2. Cancel order coffee")
        print("3. Show my order")
        print("4. Search Menu Coffee Shop Information")
        print("5. Clear Screen")
        print("6. Menu")
        print("7. About")
        print("8. Exit")
    else:
        pass