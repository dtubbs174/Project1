from pymongo import MongoClient
from random import randint

client = MongoClient()

db = client.foundationProject

names = ['Sanaa', 'Petra', 'Amirah', 'Uileag', 'Eden', 'Koresh', 'Floriana', 'Ghaliya', 'Waldomar', 'Anan', 'Tim', 'Nevio', 'Laelia', 'Ubirajara', 'Elpis', 'Danka', 'Mathys', 'Basya', 'Zahi', 'Sefanija']

for x in range(1,11):
    account = {
        'accountNum' : x,
        'name' : names[randint(0, (len(names)-1))],
        'balance' : randint(0, 100000) + (randint(0,99) * 0.01)
    }

    result = db.accounts.insert_one(account)

    print(f'Created {x} of 10 as {result.inserted_id}.')

print("Finished creating 10 bank accounts")
