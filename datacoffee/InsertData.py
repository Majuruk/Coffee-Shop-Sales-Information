# This Module has the Functions to Insert the Data in the MySQL Tables

#Importing Required Modules

# import csv
# import mysql.connector as con

# # Functions


def InsertDataCoffee():
    """
    InsertDataCoffee() -> Insert all the Coffee details in the coffee_info Table

    Parameter -> None
    """

    mn = con.connect(host="localhost",
                     user="root",
                     password="123456789",
                     database="coffeeshop")
    
    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the absolute path of the file on your computer
    try:
        with open("Dataset/coffee_shop_sales.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO coffee_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    except FileNotFoundError:
        print("please check whether file is in the Dataset Folder or not and try changing the location in InsertData.py")
    finally:
        mn.commit() # Important: Committing the changes
        cur.close()
        mn.close()
