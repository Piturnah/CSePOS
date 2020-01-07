import record_sale as r
import csv


def reciet(priceDict, bill):
    #used to from, and print the reciet
    print('''____This is the Reciet____
Items:''')
    for name in priceDict:
        print(name + ": £" + str(priceDict[name] / 100))
        
    total_print = float(bill)/100 #from p to £-p    
    print('\nTotal: £' + str(total_print))



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
            barcodes.append(barcodes)
            stock_update(barcode) #sending items to stock
            
    new_sale = r.RecordSale(barcodes) #sends items to get list of the items
    names = new_sale.getPurchases()
    bill = new_sale.getTotalBill()

    print('Total to pay: £' + float(bill)/100)
    
    
    new_sale.takePayment(bill, 0) # change second argument later
    
    reciet(new_sale.getNamesAndPrices(), bill)


def main_menu():
    #This is the main menu
    print('''   _____Main_Menu____
    1.Make transation
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
