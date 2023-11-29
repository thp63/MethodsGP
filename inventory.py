import sqlite3
import sys

class Inventory:
    def __init__(self, databaseName = "", tableName = ""):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory():
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Connection Failed")
            sys.exit()
        cursor = connection.cusor()
        cursor.execute("SELECT * FROM Inventory")
        result = cursor.fetchall()
        for i in result:
            for j in i:
                print(j, end = " | ")
            print("\n\n")

        cursor.close()
        connection.close()

    def searchInventory():
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Could not connect")
            sys.exit()

        cursor = connection.cursor()
        title = input("Enter a title: ")
        query = "SELECT * FROM Inventory WHERE Title=?"
        cursor.execute(query, title)
        result = cursor.fetchall()

        if not result:
            print("No results")
        else:
            for x in result:
                for y in x:
                    print(y, end = " | ")
                print()

        cursor.close()
        connection.close()
                
    def decreaseStock(self, ISBN):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Could not connect")
            sys.exit()
        cursor = connection.cursor()
        query = "SELECT Stock FROM Inventory WHERE ISBN=?"
        cursor.execute(query, ISBN)
        result = cursor.fetchall()

        stock = result[0][0]
        stock -= 1

        query = "UPDATE Inventory SET Stock=? WHERE ISBN=?"
        cursor.execute(query, stock, ISBN)
        connection.commit()
        cursor.close()
        connection.close()
