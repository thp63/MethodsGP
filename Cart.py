import sqlite3
import inventory
import sys

class Cart:

    def __init__(self, databaseName = 0, tableName = 0):
        self.databaseName = databaseName
        self.tablename = tableName

    def viewCart(self, userID, inventoryDatabase):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            print("Database Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cart")
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()
        connection.close()
        return

    def addToCart(self, userID, ISBN):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            print("Database Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CART (UserID, ISBN, Quantity) VALUES (" + userID + ", " + ISBN + ", 1)")
        connection.commit()
        cursor.close()
        connection.close()
        return

    def removeFromCart(self, userID, ISBN):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            print("Database Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Cart WHERE UserID=" + userID + ", ISBN=" + ISBN)
        cursor.close()
        connection.close()
        return

    def checkOut(self, userID):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except: 
            print("Database Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        decreaseInvetory(ISBN)
        cursor.execute("DELETE * FROM Cart WHERE UserID=" + userID)
        cursor.close()
        connection.close()
        return
