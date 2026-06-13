# Rock Paper Scissors :

A simple but structured Rock Paper Scissors game built in Python.  
This project started as a basic script and slowly turned into a modular CLI game with history tracking and statistics.

------------------------------------------------------------------------------------------

## Features:

- Play Rock Paper Scissors against the computer
- Persistent game history saved in a text file
- View full match history
- See win / loss / draw statistics
- Clean menu-based navigation system
- Option to quit anytime during gameplay or menus

------------------------------------------------------------------------------------------

## What I Learned:

This project helped me understand a lot more than just basic Python syntax.

Some key things I picked up:

- Splitting a program into multiple modules (`main`, `menu`, `game`, `data_info`)
- File handling (reading and writing game history)
- Input validation and handling unexpected user input
- Working with loops in a structured way instead of messy repetition
- Basic program flow control between functions and modules
- Debugging real issues (like file errors, wrong returns, and loop recursion problems)

It also made me realize how small design decisions (like return values) can affect the whole program flow.

------------------------------------------------------------------------------------------

## Project Structure:
- main.py → Controls the main game loop
- menu.py → Handles user menu and navigation
- game.py → Game logic (RPS mechanics)
- data_info.py → File handling + statistics
- history.txt → Stores game results

##  How to Run:
Just run:

```bash
python main.py
```



