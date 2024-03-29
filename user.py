import sqlite3
import sys

class User:
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.userId =""
        self.loggedIn = False
    def login(self):
        #ask for creds
        attemptedId = input("User ID: ")
        attemptedPass = input("Password: ")
        #connect to DB and search for matching
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("SELECT UserID, Password FROM User WHERE UserID=? AND Password=?", (attemptedId, attemptedPass))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        if not result:
            print("User ID or password incorrect")
            return False
        else:
            self.userId = result[0][0]
            self.loggedIn = True
            return True
    def logout(self):
        self.loggedIn = False
        self.userId = ""
        return True
    def viewAccountInformation(self):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            print("Database Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User WHERE UserID=?", (self.userId,))
        result = cursor.fetchall()
        for row in result:
            for value in row:
                print(value)
        cursor.close()
        connection.close()
        return
    def createAccount(self):
        #Have to get all the values for creating account

        # Validate User ID
        while True:
            self.userId = input("User ID: ")
            if not self.userId.isalnum():
                print("User ID must be a number.")
            else:
                break

        self.email = input("Email: ")

        # Validate Password
        while True:
            self.password = input("Password: ")
            if not self.password.isalnum():
                print("Password must only contain letters and numbers")
            else:
                break

        # Validate First Name and Last Name
        while True:
            self.Fname = input("First Name: ")
            self.Lname = input("Last Name: ")
            if not (self.Fname.isalpha() and self.Lname.isalpha()):
                print("First and Last Names must contain only letters.")
            else:
                break

        self.address = input("Address: ")
            
        
        #Validate City
        while True:
            self.city = input("City: ")
            if not self.city.isalpha():
                print("Invalid City")
            else:
                break
        
        #Validate State
        while True:
            self.state = input("State: ")
            if not self.state.isalpha():
                print("Invalid State")
            else:
                break
            
        # Validate Zip 
        while True:
            self.zip = input("Zip: ")
            if not self.zip.isdigit():
                print("Zip must be a number.")
            else:
                break

        # Validate Payment 
        while True:
            self.payment = input("Payment: ")
            if not self.payment.isalnum():
                print("Payment must be Alphanumeric")
            else:
                break
        
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            print("Database Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        #Insert given info into User table
        cursor.execute("INSERT INTO User (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (self.userId, self.email, self.password, self.Fname, self.Lname, self.address, self.city, self.state, self.zip, self.payment))
        connection.commit()
        cursor.close()
        connection.close()
        return
    def getLoggedIn(self):
        return self.loggedIn
    def getUserId(self):
        return self.userId
    