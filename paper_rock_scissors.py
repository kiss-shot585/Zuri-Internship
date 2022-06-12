"""Learning how to understand the random module by simulating a rock-paper-scissors game"""

import random

while True:
    player_action = input("Select a choice (Rock, Paper, Scissors): ")
    
    possible_actions = ["rock", "paper", "scissors"]
    
    computer_action = random.choice(possible_actions)
    
    print(f"\nYour choice {player_action}, Computer's choice {computer_action}\n")
    
    if player_action == computer_action:
        
        print(f"Both players selected {player_action}. It is a draw")
        
    elif player_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock. You are the winner")
        else:
            print("Scissors cut paper. You have lost")
    elif player_action == "rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors. You are the winner")
        else:
            print("Paper covers the rock. You have lost")
    elif player_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper. You are the winner")
        else:
            print("Rcok smashes scissors. You have lost")
    play_again = input ("play again? (y/n): ")
    if play_again.lower() != 'y':
        break

#can be better optimised using numbers. But for now it works. IT WORKS!!!
        
        
        