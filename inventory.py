import sqlite3
import sys

class Inventory:
    def __init__(self, databaseName = 0, tableName = 0):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory():
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Connection Failed")
            sys.exit()
        cursor = connection.cusor()
        result = cursor.execute("SELECT * FROM Inventory")

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
        query = "SELECT Title, Author, Stock FROM Inventory WHERE Title=?"
        cursor.execute(query, title)
        result = cursor.fetchall()

        if not result:
                print("No results")
        else:
                for x in result:
                        for y in x:
                                print(y, end = " | ")
                        print()
                

    def decreaseStock(self, ISBN):
        pass
