"""Peter and Kit
Module responsible for recording a customer purchase

import with `import record_sale as r`
create instance with `new_sale = r.RecordSale(<list of barcodes>)`
access with `new_sale.<method>`

methods:
getPurchases() returns purchases in a sale
getTotalBill() returns the total bill in pence
takePayment(amount, customer_ID) records a payment made to db
getNames() returns list of names of the purchased items
getNamesAndPrices() returns dict of <str : int> for names and prices
"""
import sqlite3
import os
import csv


def _totalBill(purchases):

    total_price = 0
    for purchase in purchases:
        total_price += _fetchPrice(purchase)
        
    return total_price

def _fetchPrice(purchase):
    # takes SINGLE barcode and returns its price from database
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    c.execute('SELECT * FROM ProductDetails WHERE barcode=?', (purchase,))
    rows = c.fetchone()

    return rows[1]

def _fetchName(barcode):
    # takes a single barcode and returns its name from database
    product_db = sqlite3.connect('products.db')
    c = product_db.cursor()
    c.execute('SELECT * FROM ProductDetails WHERE barcode=?', (barcode,))
    rows = c.fetchone()

    return rows[2]

def _recordPayment(amount, items):
    # records transaction to db
    transaction_db = sqlite3.connect('transactions.db')
    c = transaction_db.cursor()
    c.execute('SELECT * FROM Transactions WHERE ID = (SELECT MAX(ID) FROM Transactions)')
    record = c.fetchone()

    s = ", "
    c.execute('INSERT INTO Transactions VALUES (?, ?, ?)', [record[0] + 1, amount, s.join(items)])
    transaction_db.commit()


class RecordSale:

    # class stuff
    def __init__(self, purchases):
        self._purchases = purchases

    def getNames(self):
        names = []
        for purchase in self._purchases:
            names.append(_fetchName(purchase))
        
        return names
        
    def getPurchases(self):
        return self._purchases

    def getTotalBill(self):
        return _totalBill(self._purchases)

    def getNamesAndPrices(self):
        namePriceDict = {}
        for barcode in self._purchases:
            namePriceDict[_fetchName(barcode)] = _fetchPrice(barcode)
        return namePriceDict

    def takePayment(self, amount):
        _recordPayment(amount, self.getNames())

