def input_data():
    print("YOU HAVE CHOOSEN TO PLAY THE GAME \nIF YOU WISH TO GO BACK TYPE : QUIT \nCHOOSE YOUR REGION:")
    value=input('''FOR \t\t\t PRESS
    FOREST \t\t\t 1
    TEMPLE \t\t\t 2
    COMING \t\t\t 3''').lower()
    return value

def check_input_data():

    check = input_data()

    if check in ["1", "forest"]:
        forest()

    elif check in ["2", "temple"]:
        print("\nThe temple is currently under construction.")

    elif check in ["3", "coming"]:
        print("\nThis region is coming soon.")

    elif check == "quit":
        print("\nReturning to the main menu.")

    else:
        print("\nInvalid region. Try again.")
        check_input_data()

def forest():
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
            print("The trees become thicker...")
            encounter()
            break

        elif direction == "a":
            print("\nYou move towards the left.")
            print("You find an old, abandoned campsite.")
            print("There is nothing useful here.")

        elif direction == "w":
            print("\nYou move deeper into the forest.")
            print("You hear something moving in the bushes...")
            encounter()
            break

        elif direction == "s":
            print("\nYou move backward.")
            print("You return to where you came from.")

        elif direction == "quit":
            print("\nYou return to the region selection.")
            return

        else:
            print("\nInvalid direction. Use W, A, S, or D.")


def encounter():
    print("\n" + "=" * 50)
    print("ENCOUNTER!")
    print("=" * 50)

    print("""
A creature suddenly jumps out from the bushes!

It looks like a Wolf, but something is wrong.
Its eyes glow faintly in the darkness.

The creature growls at you.
You have no choice but to fight.
""")

    battle()


def battle():
    print("\n" + "-" * 40)
    print("BATTLE START")
    print("-" * 40)

    # Temporary HP values.
    # We will replace these with the proper HP system later.
    player_hp = 100
    enemy_hp = 50

    while player_hp > 0 and enemy_hp > 0:

        print(f"\nYOUR HP: {player_hp}")
        print(f"ENEMY HP: {enemy_hp}")

        choice = input("""
1. Attack
2. Run

Choose your action: """).lower()

        if choice in ["1", "attack"]:
            print("\nYou attack the creature!")

            damage = 20
            enemy_hp -= damage

            print(f"You dealt {damage} damage!")

            if enemy_hp <= 0:
                print("\nThe creature has been defeated!")
                print("You survived the encounter.")
                print("You continue deeper into the forest...")
                break

            print("\nThe creature attacks you!")

            enemy_damage = 10
            player_hp -= enemy_damage

            print(f"The creature dealt {enemy_damage} damage!")

        elif choice in ["2", "run"]:
            print("\nYou try to escape...")

            # Prototype: running always succeeds for now.
            print("You escaped from the creature!")
            break

        else:
            print("\nInvalid choice. Choose 1 or 2.")
