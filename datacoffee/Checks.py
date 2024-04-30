# This Module  has the Functions that Verify the Requirement of the Project

# Importing Required Modules

import mysql.connector as con
from mysql.connector.errors import ProgrammingError, Error
import datacoffee.InsertData as Insert

# Function


def CheckDatabase():
    """
    CheckDatabase() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = con.connect(host="localhost", user="root",
                     database="", password="123456789")
    cur = db.cursor()
    result = None

    try:
        cur.execute("use coffeeshop;")
        print("coffeeshop in use")
    except ProgrammingError:
        print("Database does not Exist!")
        result = False
    else:
        result = True
    
    if result is True:
        print("Database exists!")
    else:
        print("Creating Database with the Required Tables..")
        print("Please be Patient!")
        cur.execute("create database coffeeshop;")
        cur.execute("use coffeeshop;")
        CreateTables()
        print("Database and Tables Created!")

    cur.close()
    db.close()


def CreateTables():
    """
    CreateTables() -> Create all the Required Tables
    
    Parameters -> None
    """

    db = con.connect(host="localhost", user="root",
                     database="coffeeshop", password="123456789")
    cur = db.cursor()

    cur.execute("use coffeeshop;")
    print("coffeeshop in use")


    try:

        cur.execute("create table coffee_info (transaction_id int NOT NULL, transaction_date Date NOT NULL, transaction_time Time NOT NULL, store_id int NOT NULL, store_location varchar(50), product_id int NOT NULL, transaction_qty int NOT NULL, unit_price int NOT NULL, Total_bill int NOT NULL, product_category varchar(50) NOT NULL, product_type varchar(100) NOT NULL, product_detail varchar(100) NOT NULL, Size varchar(20) NOT NULL, Month_Name varchar(10) NOT NULL, Day_Name varchar(10) NOT NULL, Hour int NOT NULL, Month int NOT NULL, Day_of_week int NOT NULL);")
    
        cur.execute("create table coffee_order (Transaction_id int NOT NULL Auto_increment, Transaction_date Date NOT NULL, Order_id int NOT NULL, Customer_Name varchar(30) NOT NULL, Phone varchar(20) NOT NULL, Product_category varchar(50) NOT NULL, Product_type varchar(100) NOT NULL, Size varchar(20) NOT NULL);")

    except:
        print("Table is exist!")


    cur.close()
    db.close()


def CheckConnection():
    """  
    CheckConnection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(host='localhost',
                                 database='',
                                 user='root',
                                 password='123456789'
                                 )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connect to MySQL server Version", db_Info)

    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False
    
    else:
        return True



















