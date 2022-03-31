from pymongo import MongoClient
import json

client = MongoClient()

db = client.foundationProject

def closeClient():
    client.close()
def accountNumFound(accountNum):
   
    if  db.accounts.count_documents({"accountNum": accountNum}) > 0:
    # if db.accounts.find().sort('accountNum', -1).limit(1)[0]['accountNum']:
        return True
    else:
        return False
def nextAccountNum():          
    '''
    finds accounts collection and sorts it in DSC order with a limit of one to find the most recent doc then returns that number plus 1            
    '''
    return db.accounts.find().sort('accountNum', -1).limit(1)[0]['accountNum'] + 1

def loadAccount(filename):      
    '''
    opens a json file and assigns the data to variable accountData, updates the account number with a new account number one higher than the highest previously registered     #READ
    '''
    try:
            
        with open(filename) as file:
            accountData = json.load(file)
            accountData['accountNum'] = nextAccountNum()
            db.accounts.insert_one(accountData)
            input('Successfully loaded specified bank account. \nPress Enter to return to menu.')
            return accountData
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        input("Press ENTER key to return to menu.")
    except Exception as error:
        print('Something went wrong when selecting inputed file name. {}'.format(error))
        input('Press ENTER key to return to menu')
        return None
    


def viewAccount(accountNum):    
    '''
    access accounts collection and display accountNum
    '''

    #db.accounts.find_one({'accountNum': accountNum})
    #return db.accounts.find_one({'accountNum': accountNum})
    #try:
        #db.accounts.find_one({'accountNum': accountNum})
    
    account = db.accounts.find_one({'accountNum': accountNum})
    if account is not None:
        return account
    else:
        return account
    #print(input('Account was not found. \nPress ENTER key to return to menu.'))
    #except ValueError:
        #input("Please input an account number. \nPress ENTER key to return to menu.")
    #except Exception as error:
        #print('An unexpected error occured. {}'.format(error))
        #input('Press ENTER key to return to menu.')
    
    
    
def createAccount(account):     
    '''
    initialize a new account with with accountNum equal to the nextAccountNum(), assign that to the accounts collection in MongoDB and return the account                      #CREATE
    '''
    try: 
        account['accountNum'] = nextAccountNum()
        account["name"] = str(input("Please enter your name: "))
        account["balance"] = float(input("Please enter your starting balance: "))
        db.accounts.insert_one(account)
        input(f'Account number {account["accountNum"]} successfully created. \nPress ENTER key to return to menu.')
        return account
    except ValueError as valError:
        print(valError)
        input('Account Creation Failed. \nPress ENTER key to return to menu')
        return None
    except Exception as error:
        print('Account Creation Failed. \nSomething went wrong when inputing data. \nMake sure to only put numbers in for starting balance.')
        input('Press ENTER key to return to menu.')
        return None

def deposit(accountNum, amount):
    '''
    take in the accountNum and amt to deposit, calculate new total by accessing accounts and finding the accountNum then adding the amt passed to the balance.                 #UPDATE
    Set the balance of the account as the total just assigned.
    return the updated account information
    '''
    #try:
    if amount <= 0:
        return input('Must enter amount greater than zero to deposit. \nPress ENTER key to return to menu.')
    else:
        total = db.accounts.find_one({'accountNum': accountNum})['balance'] + amount
        db.accounts.update_one({'accountNum': accountNum}, {'$set': {'balance': total}})
        input(f'Successfully deposited ${amount} into account number {accountNum}. \nPress ENTER key to return to menu.')
        return db.accounts.find_one({'accountNum' : accountNum})
    # except ValueError as valError:
    #     print(valError)
    #     input('There was an error when selecting account or selecting deposit amount. Deposit Cancelled. \nMake sure to only put numbers in for each field \nPress ENTER key to return to menu.')
    #     return None
    #except Exception as error:
        #input('Invalid data type entered. Deposit cancelled. \nMake sure to only enter numbers when selecting an account or entering a deposit amount. \nPress ENTER key to return to menu.')
        #return None
def withdraw(accountNum, amount):
    '''
    take in the accountNum and amt to withdraw, calculate new total by accenssing accounts and finding the accountNum then subtracting amt passed from the balance.            #UPDATE
    Set the balance of the accoutn as the total just assigned if >= 0.
    '''
    #if type(accountNum) is int or float and type(amount) is int or float:
        #try:
    total = db.accounts.find_one({'accountNum': accountNum})['balance'] - amount
    if total < 0:
        return input('Insufficient Funds Error: Press ENTER key to return to menu.')

    else:
        db.accounts.update_one({'accountNum': accountNum}, {'$set': {'balance': total}})
        input('Successfully withdrew funds. \nPress ENTER key to return to menu.')
        return db.accounts.find_one({'accountNum': accountNum})
        # except ValueError as valError:
        #     print(valError)
        #     input('There was an error when selecting account or selecting withdrawal amount. Withdrawal cancelled. \nMake sure to only enter numbers when selecting an account or entering withdrawal amount. \nPress ENTER key to return to menu.')
        #     return None
    # else:
    #     input('Must enter numbers only when selcting an account or entering a withdrawal amount')
    #     return None
    # except Exception as error:
    #     input('Invalid data type entered. Withdrawal Cancelled. \nMake sure to only enter numbers when selecting an account or entering a deposit amount. \nPress ENTER key to return to menu.')
    #     return None

def deleteAccount(accountNum):  
    '''
    delete one account with accountNum                                                                                                                                         #DELETE
    '''
    if accountNumFound(accountNum) == True:
        db.accounts.delete_one({'accountNum': accountNum})
        input(f'Account number {accountNum} successfully deleted. \nPress ENTER key to return to menu.')
    else:
        input('The specified account was not found. Deletion Cancelled. \nPress ENTER key to return to menu.')
    