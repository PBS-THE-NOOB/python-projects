import random

def get_computer_choice():
    computer_to_game_dict={
        1:"rock",
        2:"paper",
        3:"scissor"
    }
    computer=computer_to_game_dict[random.randint(1,3)]
    return computer

def check_user_choice(user_choice):
    return user_choice in ["rock","paper","scissor"]

def get_result(computer_choice,user_choice):
    if user_choice==computer_choice:
        return "IT IS A DRAW!"
    elif (user_choice=="rock" and computer_choice=="scissor") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissorr" and computer_choice=="paper"):
        return "YOU WIN!"
    else:
        return "YOU LOST!"

while True:
    computer_choice=get_computer_choice()
    user_choice=input("Enter your choice: ").lower()
    if check_user_choice(user_choice):
        print(get_result(computer_choice,user_choice))
        print(f"You choose:{user_choice}\nComputer choose:{computer_choice}")
        if check:=input("Do you want to continue(Y/N): ").lower()=="n":
            break
    else:
        print("Invalid Choice")





    



