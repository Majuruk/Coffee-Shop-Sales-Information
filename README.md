# Welcome to Data Coffee Shop Information

Connecting coffee shop data using Python and MySQL

## List of Content

 - [FOLDERS](#folders)
 - [ROOT FOLDER FILES](#root-folder-files)
 - [FEATURES](#features)

---------
## FOLDERS

/Dataset : Contains the data that is to be inserted in the MySQL tables in csv format
         
         Files: coffee_shop_sales.csv -> Contains all the data about the data coffee in the format 
                                        (Transaction_id, Transaction_date, Transaction_time, Store_id, Store_location, Product_id, Transaction_qty, Unit_price, Total_Bill, Product_category, Product_type, Product_detail, Size, Month Name, Day Name, Hour, Month, Day of week)

/datacoffee : Contains all the files that are required by the project to work

        Files: __init__.py -> Makes the folder to be recognized as a module
               Checks.py -> This file contains the functions that verify the requirements of the Project
               InsertData.py -> This file contains the functions to insert the data in the MySQL tables
               User_Functions.py -> This file contains the function that allow a user to perform certain task
               Other.py -> This file contains some commonly used functions
-------------------
## ROOT FOLDER FILES

main.py -> This is the main file that connects all the other modules and is used to run the project

    import  datacoffee.User_Functions  as  User
    import  datacoffee.Other  as  Other
    import  datacoffee.Checks  as  Check
    from  time  import  sleepenter code here
----------
## FEATURES

Overview: It is a Data Coffee Shop Information in which a user can Order a coffee, cancel order coffee,
          check Data Information etc. It uses MySQL as the backend database.

1.  Order coffee: The customer can the order coffee
2.  Cancel order coffee: The customer can cancel the order coffee
3.  Show my order: The customer can check their coffee orders
4.  Search Menu Coffee Shop Information:The customer can see the menu for coffee
5.  Clear Screen: Clears the terminal screen
6.  Menu: Shows the menu
7.  About: Prints the content of the file to the screen
8.  Exit: Exit the program

-------------------
