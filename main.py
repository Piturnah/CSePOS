import record_sale as r
import csv


def reciet(priceDict, bill):
    #used to from, and print the reciet
    print('''\n\n____This is the Receipt____\n
Items:\n''')
    for name in priceDict:
        print(name + ": " + "£{:,.2f}".format(priceDict[name] / 100))
        
    total_print = float(bill)/100 #from p to £-p    
    print('________________\nTotal: ' + "£{:,.2f}".format(total_print))



def transaction():
    #Used for making transactions (duh)
    item = True
    barcodes = [] #items in the shop
    while item == True:
        barcode = input('Please scan barcode: ')
        if barcode == 'n':
            item = False
        else:
            item = True
            barcodes.append(barcode)
            """undo comment below when fin v"""
            #stock_update(barcode) #sending items to stock
            
    new_sale = r.RecordSale(barcodes) #sends items to get list of the items
    names = new_sale.getPurchases()
    bill = new_sale.getTotalBill()

    print('Total to pay: ' + "£{:,.2f}".format(float(bill)/100))
    
    
    new_sale.takePayment(bill) # change second argument later
    
    reciet(new_sale.getNamesAndPrices(), bill)


def main_menu():
    #This is the main menu
    print('''\n    _____Main_Menu____
    1.Make transaction
    2.Stock check
    3.Close
    
    ''')
    menu_option = input('Option: ')
    if menu_option == '1':
        transaction()
    elif menu_option == '2':
        dbCheck(database)
    elif menu_option == '3':
        pass
    else:
        main_menu()


main_menu()
