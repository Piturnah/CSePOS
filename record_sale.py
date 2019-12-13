"""Peter and Kit
Module responsible for recording a customer purchase

import with `import record_sale as r`
create instance with `new_sale = r.RecordSale(<list of barcodes>)`
access with `new_sale.<method>`

methods:
getPurchases() returns purchases in a sale
getTotalBill() returns the total bill in pence
takePayment(amount, customer_ID) records a payment made to db
"""
import sqlite3
import os


def _totalBill(purchases):

    total_price = 0
    for purchase in purchases:
        total_price += _fetchPrice(purchase)
        
    return total_price

def _fetchPrice(purchase):
    # takes SINGLE barcode and returns its price from database
    productdb = sqlite3.connect('products.db')
    c = productdb.cursor()
    c.execute('SELECT * FROM ProductDetails WHERE barcode=?', (purchase,))
    rows = c.fetchone()

    return rows[1]

class RecordSale:

    def takePayment(amount, customer_ID):
        # record amount paid by customer in db
        pass

    # class stuff
    def __init__(self, purchases):
        self._purchases = purchases
        
    def getPurchases(self):
        return self._purchases

    def getTotalBill(self):
        return _totalBill(self._purchases)

    def dbCheck():
        if not os.path.isfile('products.db'):
            product_db = sqlite3.connect("products.db")
            c = product_db.cursor()

            c.execute('''CREATE TABLE ProductDetails
            (barcode text,
            price int,
            name text,
            stock int,
            restock_needed int
            )''')
            
            product_db.commit()
            product_db.close()