Player1 = input("Player 1: ")
Player2 = input("Player 2: ")

if Player1 == Player2:
    print("Tie")
elif Player1 == "rock":
    if Player2 == "scissors":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif Player1 == "paper":
    if Player2 == "rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    if Player2 == "paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")