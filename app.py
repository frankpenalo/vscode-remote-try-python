# Generate a complete code for the minigame called rock, paper and scissors for console.
# The game should be able to run in the console and it should have the following features:
# 1. Ask the user to choose between rock, paper and scissors.
# 2. Randomly generate one of these three options for the computer.
# 3. Compare the user's choice and the computer's choice and decide who wins.
# 4. Print the result of the game.
# 5. Ask the user if he/she wants to play again.
# 6. If the user says yes, restart the game, otherwise end the game.
# 7. Keep track of the number of wins of the user and the computer and print it after the game quits.
# 8. If the user enters an invalid option, print an error message and ask him/her to enter a valid option.
# 9. The should control the input of the user and put it in lowercase.
# 10. The program should control the input of the user and if the user enters something else than yes or no,
#     the program should ask the user to enter a valid option.

import random

computer_wins = 0
user_wins = 0
user_choice = ""

while True:
    user_choice = input("Choose (r)ock, (p)aper or (s)cissors or (q)uit: ").lower()
    if user_choice == "q":
        break
    possible_choices = ["r", "p", "s"]
    possible_choices_dict = dict(r="rock", p="paper", s="scissors")
    computer_choice = random.choice(possible_choices)

    if user_choice == computer_choice:
        print("The game is tie!")
    elif user_choice == "r":
        if computer_choice == "s":
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            computer_wins += 1
    elif user_choice == "p":
        if computer_choice == "r":
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            computer_wins += 1
    elif user_choice == "s": 
        if computer_choice == "p":
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            computer_wins += 1
    elif user_choice != "q":
        print("Please enter a valid option!")
        continue

    print(f"You chose {possible_choices_dict[user_choice]}, computer chose {possible_choices_dict[computer_choice]}.")

print(f"\nComputer score: {computer_wins}")
print(f"Your score: {user_wins}")
print("\nThanks for playing")



