import hp
import encounter
from random import randint
import time

def input_data():
    print("YOU HAVE CHOOSEN TO PLAY THE GAME \nIF YOU WISH TO GO BACK TYPE : QUIT \nCHOOSE YOUR REGION:")
    value=input('''FOR \t\t\t PRESS
FOREST \t\t\t 1
TEMPLE \t\t\t 2
COMING \t\t\t 3\n''').lower()
    return value

def check_input_data():

    while True:
        check = input_data()

        if check in ["1", "forest"]:
            hp.new_game()
            forest()
            return

        elif check in ["2", "temple"]:
            hp.new_game()
            print("\nThe temple is currently under construction.")
            return

        elif check in ["3", "coming"]:
            hp.new_game()
            print("\nThis region is coming soon.")
            return

        elif check == "quit":
            print("\nReturning to the main menu.")
            return

        else:
            print("\nInvalid region. Try again.")

def Entering_animation(phase):
    print(f"Entering {phase}", end="", flush=True)
    for _ in range(3):  
        for dots in range(4): 
            print(f"\rEntering {phase}" + "." * dots, end="", flush=True)
            time.sleep(0.5)
    print()

def forest():
    Entering_animation("Forest")
    print("\n" + "=" * 50)
    print("YOU HAVE ENTERED THE FOREST")
    print("=" * 50) 
    print("""
The trees around you are unusually quiet.
A cold wind passes through the branches.

You see four possible paths.
""")
    while True:
        direction = input("""
    MOVE:

    W -> FORWARD
    A -> LEFT
    S -> BACKWARD
    D -> RIGHT

    Enter your move: """).lower()

        if direction == "d":
            print("\nYou move towards the right.")
            if random_selector()==1:
                encounter.encounter()
                break
            print("There is nothing useful here.")

        elif direction == "a":
            print("\nYou move towards the left.")
            if random_selector()==1:
                encounter.encounter()
                break
            print("There is nothing useful here.")

        elif direction == "w":
            print("\nYou move deeper into the forest.")
            if random_selector()==1:
                encounter.encounter()
                break
            print("There is nothing useful here.")
            
        elif direction == "s":
            print("\nYou move backward.")
            print("You return to where you came from.")

        elif direction == "quit":
            print("\nYou return to the region selection.")
            return

        else:
            print("\nInvalid direction. Use W, A, S, or D.")

def random_selector():
    return randint(0,1)

