import sqlite3


class User:
    def _init_(self):
        self.userId =""
        self.loggedIn = False
    def _init_(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
    def login(self):
        self.userId = input("User ID: ")
        self.password = input("User ID: ")
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT UserID, Password FROM User WHERE UserID=" + self.userId + ", Password=" + self.password)
        result = cursor.fetchall()
        #ID result from db
        DBID = result[0][0]
        #Pass result from db
        DBPass = result[0][1]
        if DBID != self.userId or DBPass != self.password:
            if DBID != self.userId:
                print("User ID not found")
            if DBPass != self.password:
                print("Incorrect Pass")
        else:
            self.loggedIn = True
    def logout(self):
        pass
    def viewAccountInformation(self):
        pass
    def createAccount(self):
        pass
    def setPassword(self):
        self.password = input("Password: ")
    def getPassword(self):
        return self.password
    def setUserId(self):
        self.setUserId = input("User ID: ")
    def getUserId(self):
        return self.userId
    def setdbName(self):
        self.dbName
    def getdbName(self):
        return self.dbName
    def setTableName(self):
        self.tableName
    def getTableName(self):
        return self.tableName
    