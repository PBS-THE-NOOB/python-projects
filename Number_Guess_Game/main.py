from random import randint
import high_score_tracker as hst
computer=randint(1,100)
print("\t\t\t\t\t\t\t --------NUMBER GUESSING GAME----------")
guess=1
high_score=hst.get_high_score()
while True:
    print(f"Currnet guess:{guess}")
    print(f"High Score:{high_score}")
    try:
        user=int(input("Enter your guess(1-100): "))
        if user==computer:
            print("You guessed correct!")
            hst.update_high_score(guess)
            break
        elif user>computer:
            print("Too high\n")
        else:
            print("Too low\n")
        guess +=1

    except ValueError:
        print("Invalid Value! Try again.")
