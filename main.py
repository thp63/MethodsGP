#Imports
#Import User Class and create instance so it can be properly used
from user import User
user_instance = User(dbName='MethodsGPDB.db', tableName='User')

#will need to import inventory and cart in the same way as User class
from inventory import viewInventory, searchInventory, decreaseStock
from Cart import viewCart, addToCart, removeFromCart, checkOut

#Starts menu sequencing
def start():
    menuBFL()
    optionBFL = int(input("Option (0-3): "))
    while optionBFL != 0:
        if optionBFL == 1:
            print("Logging in...\n")
            if user_instance.login() == True:
                menuAFL()

        elif optionBFL == 2:
            print("Creating account...\n")
            #Call create Account from User
            user_instance.createAccount()

        elif optionBFL == 3:
            print("Logging out...\n")
            #Call Logout from user
            user_instance.logout()

        else:
            print("Invalid option! Try again!\n")
        menuBFL()
        optionBFL = int(input("Option (0-3): "))
print("Exiting...")

#Menu before Login
def menuBFL():
    print("MethodsGP Menu")
    print("(0) Exit")
    print("(1) Login")
    print("(2) Create Account")
    print("(3) Logout")

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
        else:
            print("Invalid option! Try again!\n")
        menuAFL()
        optionAFL = int(input("Option (1-4): "))

#Menu for Inventory
def menuInventory():
    print("(1) Previous")
    print("(2) View Inventory")
    print("(3) Search Inventory")
    print("(4) Decrease Stock")
    optionINV = int(input("Option (1-4): "))
    while optionINV:
        if optionINV == 1:
            menuAFL()
        elif optionINV == 2:
            viewInventory()
        elif optionINV == 3:
            searchInventory()
        elif optionINV == 4:
            decreaseStock(ISBN)
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
    optionCART = int(input("Option (1-3): "))
    while optionCART:
        if optionCART == 1:
            menuAFL()
        elif optionCART == 2:
            viewCart()
        elif optionCART == 3:
            addToCart()
        elif optionCART == 4:
            removeFromCart()
        elif optionCART == 5:
            checkOut()
        else:
            print("Invalid option! Try again!\n")
        menuCart()
        optionCART = int(input("Option (1-3): "))


#Variables

#Main
#Menu Loop
start()
