# This Module has the Function that allow a User to do Certain Task's

# Importing Required Modules
import mysql.connector
import os
import datetime
import time
from mysql.connector import DataError
import random


# Defining Some Initital Variables
current_date = datetime.date.today()


# Functions
def UpdateCoffee():
    """
    Updatecoffee() -> Update New Mobile Number coffee shop editing to the Requirement

    Parameters -> None
    """
    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456789", database="coffeeshop")
    cur = mn.cursor()

    your_name = input("Please Enter your Name: ")
    mobile_on = input("Please Enter your 10 Digit Mobile Number: ")
    new_mobile_number = input("Please Enter your new 10 Digit Mobile Number: ")

    sql = 'UPDATE coffee_order SET Phone = %s where Customer_Name= %s AND Phone= %s'

    value = (new_mobile_number, your_name, mobile_on)

    cur.execute(sql, value)

    print("Update data successfully!")

    mn.commit()
    cur.close()
    mn.close()


def ShowOrder():
    """
    ShowOrder() -> Shows the Order Made by an User

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456789", database="coffeeshop")
    cur = mn.cursor()

    mobile_on = input("Please Enter your 10 Digit Mobile Number: ")

    cur.execute('SELECT * FROM coffee_order where Phone="{}"'.format(mobile_on))

    result = cur.fetchall()
    if len(result) == 0:
        print("No Records Found!")
    else:
        order_no = 1
        print(["Transaction_id", "Transaction_date", "Order_id", "Customer_Name", "Phone", "Product_category",
                        "Product_type", "Size"])
        for x in result:
            print("Order NO", order_no, ":", x, "\n")
            order_no += 1

    cur.close()
    mn.close()


def OrderCoffee():
    """
    OrderCoffee() -> Let's a User Order a Coffee

    Parameters -> None
    """
    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456789", database="coffeeshop")
    cur = mn.cursor()

    cur.execute("USE coffeeshop;")


    # Insert Transaction_NO
    while True:
        try:
            Transaction_no = int(input("Transaction Number: "))
        except ValueError:
            print("Please Enter a Valid Transaction Number!")
            continue
        else:
            break

    # Insert Customer Name
    while True:
        Name = input("Enter your Name: ")
        if len(Name) == 0:
            print("Please Enter a Name!")
        elif len(Name) > 40:
            print("Name too long!")
        else:
            break

    # Insert Your Phone
    while True:
        try:
            Mobile = input("Enter your Mobile Number: ")
        except ValueError:
            print("Please Enter a Valid Mobile Number!")
            continue
        else:
            if len(str(Mobile)) == 10 and Mobile != 0000000000:
                break
            elif len(str(Mobile)) > 10 or len(str(Mobile)) < 10:
                print("Please Enter a Valid 10 Digit Mobile Number!")
                print("Ex. '0123456789' ")
            else:
                print("please Enter a Valid Phone Number: ")
                print("Ex. '0123456789' ")

    # Insert Product Category
    while True:
        Category = input("Enter your Product Category: ")
        if len(Category) == 0:
            print("Please Enter a Product Category")
        elif len(Category) > 50:
            print("Product Category name too long!")
        else:
            break
    
    #Insert Product Type
    while True:
        Type = input("Enter your Product Type \n(Ex. Brewed Chai tea/Gourmet brewed coffee/Barista Espresso etc.) \n: ")
        if len(Type) == 0:
            print("Please Enter a Product Type")
        elif len(Type) > 100:
            print("Product Type name too long!")
        else:
            break
    
    #Insert Product Size
    while True:
        Size = input("Enter your Product Size \n(Ex. Regular/Large/Not Defined/ Small) \n: ")
        if len(Size) == 0:
            print("Please Enter a Product Size")
        elif len(Size) > 20:
            print("Product Size name too long!")
        else:
            break
    
    Time_of_Transaction = datetime.datetime.now()
    date = Time_of_Transaction.date()
    date = date.strftime("%Y-%m-%d")

    # Creating Unique order_id for each Order coffee
    id = random.randint(1, 10000)
    cur.execute("SELECT Order_id FROM coffee_order")
    result = cur.fetchall()
    # print(result)
    Used_ID = []
    for x in result:
        for y in x:
            Used_ID.append(y)
    while True:
        if id in Used_ID:
            id = random.randint(1, 10000)
        else:
            break
    
    #check order again
    while True:
        check = input("Are you check in your order? (Y/N)")
        if check in ["Y", "y"]:
            print("Transaction_no: ",Transaction_no," Type: ",type(Transaction_no))
            print("Date: ",date," Type: ",type(date))
            print("Order_id: ",id," Type: ",type(id))
            print("Customer_name: ",Name," Type: ",type(Name))
            print("Your Phone: ",Mobile," Type: ",type(Mobile))
            print("Product_category: ",Category," Type: ",type(Category))
            print("Product_type: ",Type," Type: ",type(Type))
            print("Product_size: ",Size," Type: ",type(Size))
            break
        elif check in ["N", "n"]:
            print("Confirm on your order...")
            break
        else:
            print("Please Enter Y (Yes) or N (No)!")


    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456789", database="coffeeshop")
    cur = mn.cursor()

    cur.execute("USE coffeeshop;")

    #Sure your Order
    while True:
        ask = input("Are you Sure your Order coffee? (Y/N)")
        if ask in ["Y", "y"]:
            print("Confrim order...")
            try:
                print('Hello world')
                query = "INSERT INTO coffee_order values({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    Transaction_no, date, id, Name, Mobile, Category, Type, Size)
        
                cur.execute(query)
                mn.commit()
            except DataError:
                print("Error in ordering!")
            else:
                print("Successfully ordered!")
                cur.close()
                mn.close()
                break
        elif ask in ["N", "n"]:
            print("Stopping Ordering...")
            time.sleep(0.5)
            os.system("cls")
            break
        else:
            print("Please Enter Y (Yes) or N (No)!")
    


def CancelOrdering():
    """
    CancelOrdering() -> Allows a User to Cancel Ordering

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456789", database="coffeeshop")
    cur = mn.cursor()

    print("please use the show my Order Option\n to get the Unique ID of the Ordering you want to Cancel!")

    while True:
        try:
            unique_id = int(input("Enter the Unique ID: "))
        except ValueError:
            print("Please Enter a Valid ID!")
        else:
            if len(str(unique_id)) == 0:
                print("Invalid ID!")
            elif unique_id < 1:
                print("ID Out of Range!")
            elif unique_id > 10000:
                print("ID Out of Range!")
            elif len(str(unique_id)) != 0 and unique_id >= 1 and unique_id <= 10000:
                cur.execute(
                    "SELECT * FROM coffee_order WHERE Order_id={}".format(unique_id))
                result = cur.fetchall()
                if len(result) == 0:
                    print("NO Records Found!")
                    break
                print(["Transaction_id", "Transaction_date", "Order_id", "Customer_Name", "Phone", "Product_category",
                        "Product_type", "Size"])
                for x in result:
                    print(x)
                while True:
                    ask = input("Are you Sure you want to Cancel this(Y/N): ")
                    if ask in ["Y", "y"]:
                        cur.execute(
                            "DELETE FROM coffee_order where Order_id={}".format(unique_id))
                        print("Deleted!")
                        mn.commit()
                        cur.close()
                        mn.close()
                        break
                    elif ask in ["N", "n"]:
                        break
                    else:
                        print("Please Enter either Y (Yes) or N (NO)!")
                break
            else:
                print("Please Enter a Valid ID!")

