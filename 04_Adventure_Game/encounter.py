import random
import hp
import creature_info

def encounter():
    print("\n" + "=" * 50)
    print("ENCOUNTER!")
    print("=" * 50)

    creature_Selector=random.randint(1,len(creature_info.creatures))
    creature=creature_info.creatures[creature_Selector]
    print(f"""
A creature suddenly jumps out from the bushes!

It looks like a {creature["name"]}.

The creature growls at you.
You have no choice but to fight.
""")

    battle(creature)

def battle(creature):
    print("\n" + "-" * 40)
    print(f"BATTLE START\t\tENEMY:{creature["name"]}")
    print("-" * 40)

    player_hp = hp.give_health()
    enemy_hp = creature["hp"]

    while player_hp > 0 and enemy_hp > 0:

        print(f"\nYOUR HP: {player_hp}")
        print(f"ENEMY HP: {enemy_hp}")

        choice = input("""
1. Attack
2. Run

Choose your action: """).lower()

        if choice in ["1", "attack"]:
            print("\nYou attack the creature!")

            damage = round(random.randint(10,30)/10)*10
            enemy_hp -= damage

            print(f"You dealt {damage} damage!")

            if enemy_hp <= 0:
                print("\nThe creature has been defeated!")
                print("You survived the encounter.")
                print("You continue deeper into the forest...")
                break

            print("\nThe creature attacks you!")

            enemy_damage=creature["damage"]
            player_hp=hp.player_damage(enemy_damage)
            print(f"The creature dealt {enemy_damage} damage!")
            if player_hp==0:
                print(f"{'=' * 50}\nGAME OVER! YOU HAVE BEEN DEFEATED.\n{'=' * 50}")

        elif choice in ["2", "run"]:
            print("\nYou try to escape...")

            # Prototype: running always succeeds for now.
            print("You escaped from the creature!")
            break

        else:
            print("\nInvalid choice. Choose 1 or 2.")
