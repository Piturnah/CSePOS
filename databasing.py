import sqlite3
import os
import time

def addRecords_p(database):
    dbCheck(database) # check if db exists, if not create

    conn = sqlite3.connect(database)

    c = conn.cursor()

    if database == 'products.db':
        bar = input("Input the barcode: ")
        price = int(input("Input the price: "))
        name = input("Input the name: ")
        stock_shelves = int(input("Input current stock on the shelves: "))
        stock_back = int(input("Input the current stock that is being stored: "))
        restock = int(input("Input the restock needed value : "))

        items = [bar, price, name, stock_shelves, stock_back, restock]

    else:
        print("No record adding configured")
        quit()
        
    # additional conditionals can be used, or switch dict, to add records to other dbs

    c.execute('INSERT INTO ProductDetails VALUES (?, ?, ?, ?, ?, ?)', items)

    conn.commit()

    conn.close()


def dbCheck(database):
    # takes string containing name of db
    if not os.path.isfile(database):
        new_db = sqlite3.connect(database)
        c = new_db.cursor()

        if database == "products.db":
            c.execute('''CREATE TABLE ProductDetails
            (barcode text,
            price int,
            name text,
            stock_shelves int,
            stock_back int,
            restock_needed int
            )''')
        
        elif database == "transactions.db":
            c.execute('''CREATE TABLE Transactions
            (id int,
            time text,
            solditems text 
            )''')
            items = [1, 'Cash', 10, 2]
            c.execute('INSERT INTO Transactions VALUES (?, ?, ?, ?)', items)

        new_db.commit()

        new_db.close()
