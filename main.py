import random

print("*****Rock, Paper, Scissors Game*****")
print("******CPU vs PLAYER*****")


def game_play():
    while True:
        user_choice = input("""What is your move
        R for rock,
        P for paper,
        S for scissors \n""")
        user_choice = user_choice.upper()
        if user_choice == "R":
            user_choice = "Rock"
            break
        elif user_choice == "P":
            user_choice = "Paper"
            break
        elif user_choice == "S":
            user_choice = "Scissors"
            break
        else:
            print("Input a valid move.")

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    print("Computer is making its move ...")
    print("Player(%s):CPU(%s)" % (user_choice, computer_choice))
    # check who won
    if computer_choice == user_choice:
        print("IT'S A TIE!!!")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("YOU WIN!!!")
        else:
            print("CPU WINS!!!")
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("YOU WIN!!!")
        else:
            print("CPU WINS!!!")
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("YOU WIN!!!")
        else:
            print("CPU WINS!!!")
    restart = int(input("Will you like to play again?\n 1 for YES 2 for NO\n"))
    if restart == 1:
        game_play()
    else:
        print("Thanks for playing")


game_play()
