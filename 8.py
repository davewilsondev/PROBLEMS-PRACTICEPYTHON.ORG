"""Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
while True:
    print("Lets play a game of rocks paper scissors")
    print("Choose r for rock, p for paper and s for scissor")
    p1 = input("Player 1s pick: ")
    p2 = input("Player 2s pick: ")
    
    if p1.lower() == "r" and p2.lower() == "s":
        print("Player 1 wins")
    elif p1.lower() == "s" and p2.lower() == "r":
        print("Player 2 wins")
    elif p1.lower() == "s" and p2.lower() == "p":
        print("Player 1 wins")
    elif p1.lower() == "p" and p2.lower() == "s":
        print("Player 2 wins")
    elif p1.lower() == "p" and p2.lower() == "r":
        print("Player 1 wins")
    elif p1.lower() == "r" and p2.lower() == "p":
        print("Player 2 wins")
    elif p1.lower() == "r" and p2.lower() == "r":
        print("Its a draw")
    elif p1.lower() == "s" and p2.lower() == "s":
        print("Its a draw")
    elif p1.lower() == "p" and p2.lower() == "p":
        print("Its a draw")
    else:
        print("You didnt pick a valid char")
    
    print("Would you like to play another game? y or n")
    yn = input("pick y or n: ")
    if yn.lower() == "n": break
