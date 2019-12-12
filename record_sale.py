"""Peter and Kit
Module responsible for recording a customer purchase

import with `import record_sale`
create instance with `foo = record_sale.RecordSale(<list of barcodes>)`
access with `foo.<method>`
"""

def totalBill(purchases):

    total_price = 0
    for purchase in purchases:
        total_price += fetchPrice(purchase)
        
    return total_price

def fetchPrice(purchase):
    # takes SINGLE barcode and returns its price from database
    return 0
    
def takePayment(amount, customer_ID):
    # record amount paid by customer in db
    pass

class RecordSale:
    
    def __init__(self, purchases):
        self.purchases = purchases
        
    def getPurchases(self):
        return self.purchases

    def getTotalBill(self):
        return totalBill(self.purchases)
