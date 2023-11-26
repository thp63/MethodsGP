import sqlite3


class User:
    def _init_(self):
        self.userId =""
        self.loggedIn = False
    def _init_(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
    def login(self):
        #ask for creds
        attemptedId = input("User ID: ")
        attemptedPass = input("Password: ")
        #connect to DB and search for matching
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT UserID, Password FROM User WHERE UserID=" + attemptedId + ", Password=" + attemptedPass)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        #ID result from db
        DBID = result[0][0]
        #Pass result from db
        DBPass = result[0][1]
        #validate search
        if DBID != attemptedId or DBPass != attemptedPass:
            if DBID != attemptedId:
                print("User ID not found")
            if DBPass != attemptedPass:
                print("Incorrect Pass")
            return False
        else:
            #set variables
            self.password = attemptedPass
            self.userId = attemptedId
            self.loggedIn = True
            return True
    def logout(self):
        self.loggedIn = False
        self.userId = ""
        return
    def viewAccountInformation(self):
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User WHERE UserID=" + self.userId)
        result = cursor.fetchall()
        for x in result:
            for y in x:
                print(y)
        cursor.close()
        connection.close()
        return
    def createAccount(self):
        #Have to get all the values for creating account
        #Still need to do data validation
        self.userId = input("User ID: ")
        self.email = input("Email: ")
        self.password = input("Password: ")
        self.Fname = input("First Name: ")
        self.Lname = input("Last Name: ")
        self.address = input("Address: ")
        self.city = input("City: ")
        self.state = input("State: ")
        self.zip = input("Zip: ")
        self.payment = input("Payment: ")
        
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cursor()
        #Have to finish adding values below
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
    