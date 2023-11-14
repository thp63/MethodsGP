#Menu Function
def menu():
    print("MethodsGP Menu")
    print("(0) Exit")
    print("(1) Login")
    print("(2) Create Account")
    print("(3) Logout")

#Variables


#Main
menu()
option = int(input("Option (0-3): "))

#Menu Loop
while option != 0:
    if option == 1:
        print("Logging in...")
    elif option == 2:
        print("Creating account...")
    elif option == 3:
        print("Logging out...")
        break
    else:
        print("Invalid option! Try again!")
        option = int(input("Option (1-3): "))