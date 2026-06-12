import data_info
import game
def ask_choice():
   print("----------------GAME MENU----------------")
   print("ACTION:  ENTER: ")
   print('''PLAY GAME:  ENTER:1
PRINT HISTORY:  ENTER:2
SEE WIN/LOSS/DRAW RATE:  ENTER:3
TO QUIT   ENTER:4   \n''')
   try:
    choice=int(input("ENTER YOUR CHOICE: "))
    return choice
   except ValueError:
     return "Invalid"

def win_loss_draw():
    print("-----------------Statistics-----------------")
    print('SEE WIN RATE  | ENTER:1\nSEE LOSS RATE  | ENTER:2\nSEE DRAW RATE  | ENTER:3\n')
    try:
      choice=int(input("ENTER YOUR CHOICE: "))
      if choice==1:
        return data_info.display_rate("win")
      elif choice==2:
        return data_info.display_rate("lose")
      elif choice==3:
        return data_info.display_rate("draw")
      else:
         return "Invalid Input"
         
    except ValueError:
      return "Invalid Input"
    
def call_function():
    choice=ask_choice()
    print()
    if choice==1:
        if game.play_game() == "quit":
           call_function()
    elif choice==2:
        print(data_info.load_history())
    elif choice==3:
        while True:
            check=win_loss_draw()
            if check=="Invalid Input":
                print("Try again! Invalid input!")
            else:
               break
        print(f"The rate is: {check} per 100 games.")
    elif choice==4:
       return "quit"
    elif choice=="Invalid":
       return "Invalid"
    
        





  