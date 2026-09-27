#tasks create a simple menu:
import time
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

def direct_location(check):
    if check==1:
        print('Game Menu')
        print("""Choose Phase: Enter the corresponding phase""")
    elif check==2:
        pass
    elif check==3:
        pass
    elif check==4:
        pass

def Entering_animation(phase):
    print(f"Entering {phase}", end="", flush=True)
    for _ in range(3):  
        for dots in range(4): 
            print(f"\rEntering {phase}" + "." * dots, end="", flush=True)
            time.sleep(0.5)
    print()  





