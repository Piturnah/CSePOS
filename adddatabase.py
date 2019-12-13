import sqlite3
from record_sale import RecordSale

RecordSale.dbCheck()

conn = sqlite3.connect('products.db')

c = conn.cursor()

bar = input("Input the barcode: ")
price = int(input("Input the price: "))
name = input("Input the name: ")
stock = int(input("Input current stock: "))
restock = int(input("Input the restock needed value : "))

items = [bar, price, name, stock, restock]

c.execute('INSERT INTO ProductDetails VALUES (?, ?, ?, ?, ?)', items)

conn.commit()

conn.close()