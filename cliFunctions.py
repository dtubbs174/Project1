from pymongo import MongoClient
import json

client = MongoClient()

db = client.foundationProject

def closeClient():
    '''
    Close the database client collection
    '''
    client.close()
def accountNumFound(accountNum):
    '''
    Checks accounts collection to see if the account number entered exists previously
    '''
    if  db.accounts.count_documents({"accountNum": accountNum}) > 0:
    
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

    
    
    account = db.accounts.find_one({'accountNum': accountNum})
    if account is not None:
        return account
    else:
        return account
    
    
    
    
def createAccount(account):     
    '''
    initialize a new account with with accountNum equal to the nextAccountNum(), assign that to the accounts collection in MongoDB and return the account                      #CREATE requirement met
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
    except:
        print('Account Creation Failed. \nSomething went wrong when inputing data. \nMake sure to only put numbers in for starting balance.')
        input('Press ENTER key to return to menu.')
        return None

def deposit(accountNum, amount):
    '''
    take in the accountNum and amt to deposit, calculate new total by accessing accounts and finding the accountNum then adding the amt passed to the balance.                 #UPDATE requirement met
    Set the balance of the account as the total just assigned.
    return the updated account information
    '''
    
    if amount <= 0:
        return input('Must enter amount greater than zero to deposit. \nPress ENTER key to return to menu.')
    else:
        total = db.accounts.find_one({'accountNum': accountNum})['balance'] + amount
        db.accounts.update_one({'accountNum': accountNum}, {'$set': {'balance': total}})
        input(f'Successfully deposited ${amount} into account number {accountNum}. \nPress ENTER key to return to menu.')
        return db.accounts.find_one({'accountNum' : accountNum})
    
def withdraw(accountNum, amount):
    '''
    take in the accountNum and amt to withdraw, calculate new total by accenssing accounts and finding the accountNum then subtracting amt passed from the balance.            #UPDATE requirement met
    Set the balance of the accoutn as the total just assigned if >= 0.
    '''
    
    total = db.accounts.find_one({'accountNum': accountNum})['balance'] - amount
    if total < 0:
        return input('Insufficient Funds Error: Press ENTER key to return to menu.')

    else:
        db.accounts.update_one({'accountNum': accountNum}, {'$set': {'balance': total}})
        input('Successfully withdrew funds. \nPress ENTER key to return to menu.')
        return db.accounts.find_one({'accountNum': accountNum})
        

def deleteAccount(accountNum):  
    '''
    delete one account with accountNum                                                                                                                                         #DELETE requirement met
    '''
    if accountNumFound(accountNum) == True:
        db.accounts.delete_one({'accountNum': accountNum})
        input(f'Account number {accountNum} successfully deleted. \nPress ENTER key to return to menu.')
    else:
        input('The specified account was not found. Deletion Cancelled. \nPress ENTER key to return to menu.')
    