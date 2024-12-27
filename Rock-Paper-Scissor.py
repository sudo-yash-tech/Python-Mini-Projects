"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random

item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter Your Move : Rock, Paper, Scissor : ")
computer_choice = random.choice(item_list)

print(f"User Choice : {user_choice} \t Computer Choice : {computer_choice}")

if user_choice == computer_choice:
    print("Both Chooses same : Match Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper": #Paper Condition
        print("Paper will cover the Rock : Computer Win!!!")
    else:
        print("Rock will crash the Scissor : You Win!!!")
elif user_choice == "Paper":
    if computer_choice == "Scissor": #Scissor Condition
        print("Scissor will cut the Paper : Computer Win!!!")
    else:
        print("Paper will cover the Rock : You Win!!!")
elif user_choice == "Scissor":
    if computer_choice == "Rock": #Rock Condition
        print("Rock will crash the Scissor : Computer Win!!!")
    else:
        print("Scissor will cut the Paper : You Win!!!")