import sqlite3

class Inventory:
    def __init__(self, databaseName = 0, tableName = 0):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory():
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cusor()
        cursor.execute("SELECT * FROM Inventory")

    def searchInventory():
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cusor()
        answer = yes
        while answer == "yes":
            title = input("Enter the title for the book you are looking for:")
            cursor.execute("SELECT * FROM Inventory WHERE Title = %" + title + "%")
            answer = input("Would you like to search again?(yes/no): ")

    def decreaseStock(self, ISBN):
        
