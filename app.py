import random
import time
import sys
import os

# Write a prompt for the user to write between three options: rock, paper, or scissors
def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'q' to quit at any time.")
    print("Please enter one of the following:")
    print("Rock")
    print("Paper")
    print("Scissors")
    print("")

    # Get the user's input
    user_input = input("Enter your choice: ")

    # If the user's input is q, quit the game
    if user_input == "q":
        sys.exit()

    # If the user's input is not rock, paper, or scissors, restart the game
    if user_input != "Rock" and user_input != "Paper" and user_input != "Scissors":
        print("Invalid input. Please try again.")
        print("")
        main()

    # Choose a random number between 1 and 3
    random_number = random.randint(1, 3)

    # Assign a choice to the random number
    if random_number == 1:
        computer_choice = "Rock"
    elif random_number == 2:
        computer_choice = "Paper"
    elif random_number == 3:
        computer_choice = "Scissors"

    # Print the computer's choice
    print("The computer chose: " + computer_choice)

    # Print the user's choice
    print("You chose: " + user_input)

    # Print a blank line
    print("")

    # Print the winner
    if user_input == computer_choice:
        print("It's a tie!")
    elif user_input == "Rock" and computer_choice == "Paper":
        print("The computer wins!")
    elif user_input == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_input == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_input == "Paper" and computer_choice == "Scissors":
        print("The computer wins!")
    elif user_input == "Scissors" and computer_choice == "Rock":
        print("The computer wins!")
    elif user_input == "Scissors" and computer_choice == "Paper":
        print("You win!")

    # Print a blank line
    print("")

    # Add a dictionary to save how many games the user has won, lost, and tied
    # Add a dictionary to save how many games the user has won, lost, and tied
    # If the user has already played the game before, load the dictionary from a file
    if os.path.isfile("rps.txt"):
        with open("rps.txt", "r") as file:
            game_stats = eval(file.readline())
    else:
        game_stats = {
            "wins": 0,
            "losses": 0,
            "ties": 0
        }

    # Add a win to the game_stats dictionary
    if user_input == computer_choice:
        game_stats["ties"] += 1
    elif user_input == "Rock" and computer_choice == "Paper":
        game_stats["losses"] += 1
    elif user_input == "Rock" and computer_choice == "Scissors":
        game_stats["wins"] += 1
    elif user_input == "Paper" and computer_choice == "Rock":
        game_stats["wins"] += 1
    elif user_input == "Paper" and computer_choice == "Scissors":
        game_stats["losses"] += 1
    elif user_input == "Scissors" and computer_choice == "Rock":
        game_stats["losses"] += 1
    elif user_input == "Scissors" and computer_choice == "Paper":
        game_stats["wins"] += 1

    # Save the game_stats dictionary to a file
    with open("rps.txt", "w") as file:
        file.write(str(game_stats))

    # Print the game stats
    print("Wins: " + str(game_stats["wins"]))
    print("Losses: " + str(game_stats["losses"]))
    print("Ties: " + str(game_stats["ties"]))

    # Print a blank line
    print("")

    # Wait 3 seconds
    time.sleep(1)

    # Call the main function again
    main()

if __name__ == "__main__":
    main()
