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
    choice_str=(input("ENTER YOUR CHOICE(Enter 'quit' to QUIT): ")).strip()
    if choice_str.lower()=="quit":
      return "quit"
    try:
      choice=int(choice_str)
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
           return
    elif choice==2:
        print(data_info.load_history())
    elif choice==3:
        while True:
            check = win_loss_draw()
            if check=="Invalid Input":
                print("Try again! Invalid input!")
                continue
            elif check=="NO_GAME":
               print("No games played yet.")
               continue
            elif check=="quit":
               
               break
            else:
               print(f"The rate is: {check}%")
               continue
        
    elif choice==4:
       return "quit"
    elif choice=="Invalid":
       return "Invalid"

    
        





  