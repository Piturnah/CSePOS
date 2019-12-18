import record_sale as r


def transaction():
    #Used for making transactions (duh)
    item = True
    barcodes = [] #items in the shop
    while item == True
        barcode = input('Scan the barcode: ')
        if barcode == 'n':
            item = False
        barcodes.append(barcode)
        stock_update(barcodes) #sending items to stock
            
   new_sale = r.RecordSale(barcodes) #sends items to get price and stuff
        
        
        


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
        print('option 2')
    elif menu_option == '3':
        print('option 3')
    else:
        main_menu()


main_menu()
