import sqlite3
import sys

class Inventory:
    def __init__(self, databaseName = "", tableName = ""):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory(self):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Connection Failed")
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Inventory")
        result = cursor.fetchall()
        for i in result:
            for j in i:
                print(j, end = " | ")
            print("\n\n")

        cursor.close()
        connection.close()

    def searchInventory(self):
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Could not connect")
            sys.exit()

        cursor = connection.cursor()
        title = input("Enter a title: ")
        query = "SELECT * FROM Inventory WHERE Title=?"
        cursor.execute(query, (title,))
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
        print("ISBN: ", ISBN)
        try:
            connection = sqlite3.connect("MethodsGPDB.db")
        except:
            print("Error: Could not connect")
            sys.exit()
        cursor = connection.cursor()
        query = "SELECT Stock FROM Inventory WHERE ISBN=?"
        cursor.execute(query, (ISBN,))
        result = cursor.fetchall()
        if not result:
            print(f"Error: No stock information found for ISBN {ISBN}")
        else:
            current_stock = result[0][0]
            updated_stock = max(current_stock - 1, 0)
            query_update = "UPDATE Inventory SET Stock=? WHERE ISBN=?"
            cursor.execute(query_update, (updated_stock, ISBN))
            connection.commit()
            print(f"Stock decreased for ISBN {ISBN}. Updated stock: {updated_stock}")
        cursor.close()
        connection.close()
        return
