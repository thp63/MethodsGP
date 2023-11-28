import sqlite3

class Inventory:
    def __init__(self, databaseName = 0, tableName = 0):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory():
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Connection Failed")
            
        cursor = connection.cusor()
        result = cursor.execute("SELECT * FROM Inventory")

        for i in result:
            for j in i:
                print(j, end = " | ")
            print(\n\n)

        cursor.close()
        connection.close()

    def searchInventory():
        connection = sqlite3.connect("MethodsGPDB.db")
        cursor = connection.cusor()
        answer = yes
        while answer == "yes":
            title = input("Enter the title for the book you are looking for:")
            cursor.execute("SELECT * FROM Inventory WHERE Title = %" + title + "%")
            answer = input("Would you like to search again?(yes/no): ")

    def decreaseStock(self, ISBN):
        
