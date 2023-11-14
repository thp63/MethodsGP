#Menu Before Login
def menuBFL():
    print("MethodsGP Menu")
    print("(0) Exit")
    print("(1) Login")
    print("(2) Create Account")
    print("(3) Logout")

#Menu After Login
def menuAFL():
    print("() View Account Information: ")
    print("() Inventory Information")
    print("() Cart Information")
    print("() Logout")

#Menu for Inventory
def menuInventory():
    print("() Previous")
    print("() View Inventory")
    print("() Search Inventory")

#Menu for Cart
def menuCart():
    print("() Previous")
    print("() View Cart")
    print("() Add Item(s) to Cart")
    print("() Remove Item from Cart")
    print("() Check Out")


#Variables


#Main

menuBFL()
optionBFL = int(input("Option (0-3): "))

#Menu Loop
while optionBFL != 0:
    if optionBFL == 1:
        print("Logging in...\n")
        #Call login from user
        #menuAFL()
        #while optionAFL != 0:
        #    if optionAFL == 1:
                


    elif optionBFL == 2:
        print("Creating account...\n")
        #Call create Account from User

    elif optionBFL == 3:
        print("Logging out...\n")
        #Call Logout from user

    else:
        print("Invalid option! Try again!\n")
    menuBFL()
    optionBFL = int(input("Option (0-3): "))

print("Exiting...")