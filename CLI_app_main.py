


from ssl import Options
import json

#POS/inventory for an ecommerce site



# def menu():
#     print("Welcome to Drake's Store!")
#     print('1) Load Data') #admin
#     print('2) Place an order') # customer
#     print('3) Change an order') #customer
#     print('4) Cancel an order') #customer
#     print('5) Look up a previous order') #manager
#     print('6) Take inventory') #manager
#     print('7) Place an order to replenish stock of products') #manager
#     print('8) Remove item from prodcuts list') #manager
#     print('0) Press 0 to Exit.') #all
#     optionSelected = int(input('Select menu option: '))
#     return optionSelected

def main():
    '''
    Function for selecting menu item from CLI app.
    '''
    while(True):
        optionSelected = menu()
        if(optionSelected == 0):  #exit program
            break
        if(optionSelected == 1):  #select JSON file to load
            print('You have selected option 1 to load data...')
        elif(optionSelected == 2):  #bring up order fields for user entry
            print('You selected option 2 to place an order...')
        elif(optionSelected == 3):  #list products for customer to choose from, when they type a product name ask for quantity and display order price at end
            print('You have selected change an order...')
        elif(optionSelected == 4):  #ask customer for order number, ask customer what they want to change and value to change it to
            print('You have selected cancel an order...')
        elif(optionSelected == 5):  #ask customer for order number to cancel
            print('You have selected look up a previous order...')
        elif(optionSelected == 6):  #ask customer for order number to display
            print('You have selected take inventory...')
        elif(optionSelected == 7):  #show current product list with inventory
            print('You have selected place an order to replenish stock of products...')
        elif(optionSelected == 8):  #increase stock quantity of product specified by quantity specified
            print('YOu have selected remove an item from products list')
        else:
            print('invalid option. Try again...')
            
if __name__ == '__main__':
    main()

options = []
def __init__(self, options):
    if options:
        self.options = options.copy()
        i=0
        for option in options:
            self.checklists[i] = option
            i += 1
    else:
        raise Exception("Please enter a valid option.")

# options = []
# def __init__(self, options):
#     if options:
#         self.options = options.copy()
#         i=0
#         for option in options:
#             self.checklists[i] = option
#             i += 1
#     else:
#         raise Exception("Please enter a valid option.")