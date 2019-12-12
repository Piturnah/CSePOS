class RecordSale:
    purchases = [] # list of barcode strings

    def totalBill(purchases):

        total_price = 0
        for purchase in purchases:
            total_price += fetchPrice(purchase)
        
        return total_price

    def fetchPrice(purchase):
        # takes SINGLE barcode and returns its price from database
        pass
    
    def takePayment(amount, customer_ID):
        # record amount paid by customer in db
        pass

    
    def __init__(self, purchases):
        self.purchases = purchases
        
    def getPurchases():
        return purchases

    def getTotalBill():
        return totalBill(purchases)
