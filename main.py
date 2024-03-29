#Imports
import sys
#Import User Class and create instance so it can be properly used
from user import User
user_instance = User(dbName='MethodsGPDB.db', tableName='User')

#will need to import inventory and cart in the same way as User class
from inventory import Inventory
inventory_instance = Inventory(databaseName='MethodsGPDB.db', tableName='Inventory')

#Imports Cart class and creates it's instance
from Cart import Cart
cart_instance = Cart(databaseName='MethodsGPDB.db', tableName='Cart')

#Starts menu sequencing
def start():
    menuBFL()
    optionBFL = int(input("Option (0-2): "))
    while optionBFL != 0:
        if optionBFL == 1:
            print("Logging in...\n")
            if user_instance.login() == True:
                menuAFL()

        elif optionBFL == 2:
            print("Creating account...\n")
            #Call create Account from User
            user_instance.createAccount()

        else:
            print("Invalid option! Try again!\n")
        menuBFL()
        optionBFL = int(input("Option (0-2): "))
    print("Exiting...")
    sys.exit()

#Menu before Login
def menuBFL():
    print("MethodsGP Menu")
    print("(0) Exit")
    print("(1) Login")
    print("(2) Create Account")

#Menu After Login
def menuAFL():
    print("(1) View Account Information: ")
    print("(2) Inventory Information")
    print("(3) Cart Information")
    print("(4) Logout")
    optionAFL = int(input("Option (1-4): "))
    while optionAFL:
        if optionAFL == 1:
            user_instance.viewAccountInformation()
        elif optionAFL == 2:
            menuInventory()
        elif optionAFL == 3:
            menuCart()
        elif optionAFL == 4:
            user_instance.logout()
            start()
        else:
            print("Invalid option! Try again!\n")
        menuAFL()
        optionAFL = int(input("Option (1-4): "))
#Menu for Inventory
def menuInventory():
    print("(1) Previous")
    print("(2) View Inventory")
    print("(3) Search Inventory")
    optionINV = int(input("Option (1-4): "))
    while optionINV:
        if optionINV == 1:
            menuAFL()
        elif optionINV == 2:
            inventory_instance.viewInventory()
        elif optionINV == 3:
            inventory_instance.searchInventory()
        else:
            print("Invalid option! Try again!\n")
        menuInventory()
        optionINV = int(input("Option (1-4): "))

#Menu for Cart
def menuCart():
    print("(1) Previous")
    print("(2) View Cart")
    print("(3) Add Item to Cart")
    print("(4) Remove Item from Cart")
    print("(5) Check Out")
    optionCART = int(input("Option (1-5): "))
    while optionCART:
        if optionCART == 1:
            menuAFL()
        elif optionCART == 2:
            cart_instance.viewCart(user_instance.userId, inventory_instance)
        elif optionCART == 3:
            inventory_instance.viewInventory()
            cart_instance.addToCart(user_instance.userId, input("Enter ISBN to Add: "))
        elif optionCART == 4:
            cart_instance.viewCart(user_instance.userId, inventory_instance)
            cart_instance.removeFromCart(user_instance.userId, input("Enter ISBN to Remove: "))
        elif optionCART == 5:
            cart_instance.checkOut(user_instance.userId)
        else:
            print("Invalid option! Try again!\n")
        menuCart()
        optionCART = int(input("Option (1-5): "))

#Starts Main/Menu Loop
start()
