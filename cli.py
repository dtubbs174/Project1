#from multiprocessing.sharedctypes import Value
from cliFunctions import closeClient, loadAccount, viewAccount, createAccount, deposit, withdraw, deleteAccount, accountNumFound




def menu():
    '''
    This is the menu of options for the banking CLI application.
    '''
    print("Welcome to Drake's Bank!")
    print('1) Load Bank Account') 
    print('2) View Account') 
    print('3) Create an Account') 
    print('4) Deposit') 
    print('5) Withdraw') 
    print('6) Delete Account') 
    print('0) Press 0 to Exit.') 
    try:
        optionSelected = int(input('Select menu option: '))
        return optionSelected
    except ValueError:
        input("The input was not a valid menu option. Please try again. \nPress ENTER key to return to menu.")
    except Exception as error:
        print('An unexpected error occured. {}'.format(error))
        input('Press ENTER key to return to menu.')

def main():
    '''
    Function for selecting menu item from CLI app, setting up variables to pass to functions, and executing those functions necessary to accomplish the requested menu task.
    '''
    while(True):
        optionSelected = menu()
        if(optionSelected == 0):                                                #Exit application
            closeClient()
            break
        if(optionSelected == 1):                                                #Create new account by loading an existing JSON file containing basic account info
            print('You have selected option 1 to load an account...')
            filename = input('Please enter account filename: ')
            loadAccount(filename)
            
            
        elif(optionSelected == 2):                                              #View an account using the account number
            print('You selected option 2 to view an account...')
            accountNum = int(input('Please enter your account number: '))
            account = viewAccount(accountNum)
            
            if accountNumFound(accountNum) == True:
                input(f'Account number: {account["accountNum"]} \n Name on Account: {account["name"]} \n Balance: {account["balance"]} \nPress ENTER key to return to menu.')
            else:
                input('The specified account was not found. \nPress ENTER key to return to menu.')

        elif(optionSelected == 3):                                              #Create an account by having the user enter basic details
            print('You have selected option 3 to create an account...')
            account = {}
            createAccount(account)
            
            
        elif(optionSelected == 4):                                              #Deposit an amount into an account
            print('You have selected option 4 to make a deposit ...')
            try:
                accountNum = int(input("Which account number would you like to make a deposit to?: "))
                amount = float(input("How much would you like to deposit to this account?: "))
                deposit(accountNum, amount)
            except ValueError as valError:
                print(valError)
                input('There was an error when selecting an account or selecting deposit amount. Deposit cancelled. \nMake sure to only enter numbers when selecting an account or entering deposit amount. \nPress ENTER key to return to menu.')
            
        elif(optionSelected == 5):                                              #Withdraw an amount from an account
            print('You have selected option 5 to make a withdrawal...')
            try:
                accountNum = int(input('Which account number would you like to make a withdraw from?: '))
                amount = float(input("How much would you like to withdraw from this account?: "))
                withdraw(accountNum, amount)
            except ValueError as valError:
                print(valError)
                input('There was an error when selecting an account or selecting withdrawal amount. Withdrawal cancelled. \nMake sure to only enter numbers when selecting an account or entering withdrawal amount. \nPress ENTER key to return to menu.')
            
        elif(optionSelected == 6):                                              #Delete any account
            print('You have selected opotion 6 to delete an account...')
            try:
                accountNum = int(input('Please enter an account number to delete: '))
                deleteAccount(accountNum)
            except ValueError as valError:
                print(valError)
                input('There was an error when selecting an account for deletion. Deletion Cancelled. \nMake sure to enter a valid account number. \nPress ENTER key to return to menu.')
        else:
            input('You have inputed an invalid option. Try again. \n(Press ENTER key to return to menu)')
            
            
if __name__ == '__main__':
    main()

