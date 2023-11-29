import sqlite3
from inventory import Inventory
inventory_instance = Inventory(databaseName='MethodsGPDB.db', tableName='Inventory')
import sys

class Cart:

    def __init__(self, databaseName = "", tableName = ""):
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
        query = "INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (?, ?, 1)"
        values = (userID, ISBN)
        cursor.execute(query, values)
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
        query = "DELETE FROM Cart WHERE UserID=? AND ISBN=?"
        values = (userID, ISBN)
        cursor.execute(query, values)
        connection.commit()
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
        query = ("SELECT 'ISBN' FROM Cart WHERE UserID=?")
        values = ((userID,))
        cursor.execute(query, values)
        result = cursor.fetchall()
        if not result:
            print("Nothing in Cart")
            return
        else:
            inventory_instance.decreaseStock(result[0][0])
        query = ("DELETE FROM Cart WHERE UserID=?")
        values = ((userID,))
        cursor.execute(query,values)
        cursor.close()
        connection.close()
        return
