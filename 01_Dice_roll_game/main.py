import random 
while True:
    
    check=input("Do you want to roll the dice?(Y/N): ").lower()
    if check=="y":
        i=random.randint(1,6)
        j=random.randint(1,6)
        print(f"({i},{j})")
            
    elif check=="n":
        print("Thank you for playing the game!")
        break
    else:
        print("Invalid choice!")
        

                


            
    
