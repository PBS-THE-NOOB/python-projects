#for saving computer,user choices and game conclusion 
def init_file():
    try:
        open("history.txt", "x").close()
    except FileExistsError:
        pass

def load_history():
    history=""
    with open("history.txt", "r") as f:
        for i,line in enumerate(f,start=1):
            user_choice,computer_choice,result=line.strip().split(",")
            history += (f"Game {i}. You: {user_choice} | Computer: {computer_choice} | Result: {result}\n")
    return history

def save_history(user_choice,computer_choice,result):
    if result=="YOU WIN!":
        result_modified="win"
    elif result=="IT IS A DRAW!":
        result_modified="draw"
    else:
        result_modified="lose"
    
    with open("history.txt", "a") as f:
        line_of_data=f"{user_choice},{computer_choice},{result_modified}\n"
        f.write(line_of_data)
        
def get_values(x):
    values = []
    with open("history.txt", "r") as f:
        for line in f:
            user, computer, result = line.strip().split(",")
            data = {
                "user": user,
                "computer": computer,
                "result": result
            }
            values.append(data[x])
    return values

def display_rate(key_word):
    x = get_values("result")
    count= x.count(key_word)
    return count / len(x) * 100









