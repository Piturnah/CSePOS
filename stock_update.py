# Stock Update
# Function informtaion:
# _fetch - imported from Team A's code, it takes a SINGLE barcode and returns something about it (this is dictated by "num") from database
# backroom_reorder - checks if there is enough stock in the backroom
# shelf_reorder - checks if there is enough stock in the shelves
# update_query - this updates the column called 'column' in the database at line 'barcode', changing it to 'changeto' 
# update_stock - manages the above function
# stock_update - main program called by Spencer (i.e. Team D)
# stock_return - allows someone to view the current stock of all items in the database

import sqlite3
import os
from utility import pit_ml as ml

def _fetch(purchase,num):
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    c.execute('SELECT * FROM ProductDetails WHERE barcode=?', (purchase,))
    rows = c.fetchone()
    c.close()
    return rows[num]

def backroom_reorder(barcode):
    instock = _fetch(barcode,4)
    restocklimit = _fetch(barcode,5)
    if instock < restocklimit:
        return "Need restock for backrooms"
    else:
        return "No restock for backrooms needed"

def shelf_reorder(barcode):
    instock = _fetch(barcode,3)
    if instock < 1:
        return "Need restock for shelves"
    else:
        return "No restock for shelves needed"

def update_query(barcode,column,changeto):
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    print(changeto)
    c.execute('UPDATE ProductDetails SET '+column+' = '+changeto+' WHERE barcode=?', (barcode,))
    product_db.commit()
    c.close()

def update_stock(barcode):
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    shelftemp = str(int(_fetch(barcode,3)) -1)
    backroomtemp = str(int(_fetch(barcode,4)) -1)
    update_query(barcode,'stock_shelves',shelftemp)
    update_query(barcode,'stock_back',backroomtemp)
    product_db.commit()
    print("Stock updated Succesfully")
    c.close()

def stock_update(barcodes):
    for i in range(0,len(barcodes)):
        update_stock(barcodes[i])
        backroomtemp = backroom_reorder(barcodes[i])
        shelftemp = shelf_reorder(barcodes[i])
        print("Restock checked Succesfully")
        restockstate = ("Item: " + str(barcodes[i]) + "\n" + backroomtemp + "\n" + shelftemp + "\n")
    return restockstate
    

def stock_return():
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    barcodes = [barcode[0] for barcode in c.execute("SELECT barcode FROM ProductDetails")]
    stockList = "NAME.SHELF STOCK.BACK STOCK\n\n"
    for n in range (0,len(barcodes)):
        tempbarcode = barcodes[n]
        name = _fetch(tempbarcode,2)
        shelftemp = _fetch(tempbarcode,3)
        backroomtemp = _fetch(tempbarcode,4)
        stockList = stockList + str(name) + "." + str(shelftemp) + "." + str(backroomtemp) + "\n"
    return ("\n" + ml.col(stockList, "", just="r", delimiter = "."))

if __name__ == "__main__":
    print(stock_return())
