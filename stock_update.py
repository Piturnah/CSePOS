# Stock Update
# Function informtaion:
# _fetch - imported from Team A's code, it takes SINGLE barcode and returns something about it (this is dictated by "num") from database
# backroom_reorder - checks if there is enough stock in the backroom
# shelf_reorder - checks if there is enough stock in the shelves
# update_query - this updates the column called 'column' in the database at line 'barcode', changing it to 'changeto' 
# update_stock - manages the above function
# stock_update - main program called by Spencer (i.e. Team D)
# stock_return - allows someone to view the current stock of all items in the database

import sqlite3
import os

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
    c.execute('UPDATE ProductDetails SET ? = ? WHERE barcode = ?', (column,changeto,barcode))
    c.close()

def update_stock(barcode):
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    shelftemp = _fetch(barcode,3)
    backroomtemp = _fetch(barcode,4)
    update_query(barcode,'stock_shelves int',str(int(sheltemp) - 1))
    update_query(barcode,'stock_back int',str(int(backroomtemp) - 1))
    sqliteConnection.commit()
    print("Stock updated Succesfully")
    c.close()

def stock_update(barcode):
    update_stock(barcode)
    backroomtemp = backroom_reorder(barcode)
    shelftemp = shelf_reorder(barcode)
    print("Restock checked Succesfully")
    restockstate = ("Item: " + str(barcode) + "\n" + backroomtemp + "\n" + shelftemp)
    return restockstate
    

def stock_return():
    texttoreturn = "Barcode   Shelf Stock   Backroom Stock\n<><><><><><><><><><><><>\n"
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    barcodes = [barcodes[0] for barcodes in c.execute("SELECT barcodes FROM ProductDetails")]
    for n in range (0,len(barcodes)):
        tempbarcode = barcodes[n]
        shelftemp = _fetch(tempbarcode,3)
        backroomtemp = _fetch(tempbarcode,4)
        texttoreturn = texttoreturn + str(tempbarcode) + ":   " + str(shelftemp) + "   " + str(backroomtemp) + "\n"
    return (texttoreturn +  "\n<><><><><><><><><><><><>")
