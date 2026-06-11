def update_high_score(guess):
    if guess < get_high_score():
        with open("high_score.txt", "w") as file:
            file.write(str(guess))
            
def get_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return float("inf")