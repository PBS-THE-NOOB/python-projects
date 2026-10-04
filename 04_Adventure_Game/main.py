#tasks create a simple menu:
import game
from stats import player
def menu():
    while True:
        print("="*50+"\n"+' '*20+"GAME MENU\n"+"="*50)
        print('''Play game \tPress:"1"
View Stats \tPress:"2"
Go to Shop \tPress:"3"
Quit       \tPress:"4"\n''')
        try:
            check=int(input("Enter your choice:"))
            if check in [1,2,3,4]:
                return check
            else:
                print("Not On The List!Try Again!")
        except ValueError:
            print("Invalid Input")

def direct_location(check):
    if check==1:
        game.check_input_data()
    elif check==2:
        player_stats()
    elif check==3:
        pass
    elif check==4:
        return False
    return True

def start_game():
    running=True
    while running:
        get_value=menu()
        running=direct_location(get_value)

def player_stats():
    print("="*50+"\n"+" "*15+"PLAYER STATISTICS\n"+"="*50)
    print_stats()
    input("\nPress Enter to return to the menu: ")
    print()

def print_stats():
    print(f"Player HP: {player.player_health}")
    print(f"Player Minimum Damage: {player.player_min_damage}")
    print(f"Player Maximum Damage: {player.player_max_damage}")
    print(f"Damage Boost: {player.damage_boost}")
    print(f"Defence Boost: {player.defence_boost}")
    print(f"Attack Level: {player.attack_level}")

start_game()

