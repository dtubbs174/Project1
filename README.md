# Foundation Project

## Project Description
A Python CLI (Command Line Inteface) application to showcase CRUD functionality between Python and MongoDB. Theme is based on a banking application without discriminating between what would be the user's authorization level of access. For e.g.; a customer, a teller, and a manager would have access to different levels of the system in reality but this application lets any user access every ability of the application. In addition to this, I have included a "bankAccountGenToDB.py" program which can be used to create 10 accounts with random details if there are no accounts created already.

## Technologies Used
- Python - version 3.7.7 
- File I/O 
- Collections 
- MongoDB - version 5.06 Community
- PyMongo - version 4.02
- git - version 2.35.1.windows.2

## Features
- Create a new account by loading info from a JSON file
- View an account
- Create a new account
- Deposit to an account 
- Withdraw from an account
- Delete an account from the database

## Getting Started
- Download the repository files: 
    git clone https://github.com/dtubbs174/Project1.git
- Install MongoDB Server 5.0 for your operating system: 
    https://www.mongodb.com/docs/manual/installation/
- Install PyMongo: 
    pip install pymongo

### Windows
- Create the directory for MongoDB to store files (this is the default location and can be changed): 
    cd C:\
    md data\db
- Open a cmd promt and run the following to start the MongoDB server:
    "C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe" --dbpath="c:\data\db"

### Ubuntu
- Run MongoDB Server:
    sudo sytemctl start mongod

## Usage
- Navigate to the repository directory
- Before running the main program if you wish to create 10 accounts to have data in the database run: bankAccountGenToDB.py
- Start the program with: python cli.py
- Any JSON files to be loaded must be in the same directory as the application.
- You must enter the entire JSON file name (including the .json) to load the account.
- When the program is running you will see a menu of options to choose from.

## License
This project uses the MIT License