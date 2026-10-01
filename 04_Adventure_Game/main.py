#tasks create a simple menu:
import game
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
    except ValueError:
        print("Invalid Input")
        menu()
def start_game():
    get_value=menu()
    direct_location(get_value)

def direct_location(check):
    if check==1:
        game.check_input_data()
    elif check==2:
        pass
    elif check==3:
        pass
    elif check==4:
        pass

start_game()

