#tasks create a simple menu:
import game
def menu():
    while True:
        print("="*50+"\n"+' '*20+"GAME MENU\n"+"="*50)
        print('''Play game \tPress:"1"
View Settings \tPress:"2"
View Stats \tPress:"3"
Go to Shop \tPress:"4"
Quit       \tPress:"5"\n''')
        try:
            check=int(input("Enter your choice:"))
            if check in [1,2,3,4,5]:
                return check
            else:
                print("Not On The List!Try Again!")
        except ValueError:
            print("Invalid Input")

def direct_location(check):
    if check==1:
        game.check_input_data()
    elif check==2:
        pass
    elif check==3:
        pass
    elif check==4:  
        pass
    elif check==5:
        return False
    return True

def start_game():
    running=True
    while running:
        get_value=menu()
        running=direct_location(get_value)

start_game()

