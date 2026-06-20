#tasks create a simple menu:
def menu():
    print("GAME MENU\n")
    print('''Play game? Press:"1"
View Settings? Press:"2"
View Stats? Press:"3"
Go to Shop? Press:"4"\n''')
    try:
        check=int(input("Enter your choice:"))
        if check in [1,2,3,4]:
            return check
        else:
            print("Not On The List!Try Again!")
            menu()
    except ValueError:
        print("Invalid Input")
        menu()

menu()