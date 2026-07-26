import random
comp_choice = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
tries = 5

choices = {
    "1": "rock",
    "2": "paper",
    "3": "scissors",
}

while tries > 0:
    random_comp_choice = random.choice(comp_choice)
    # print(random_comp_choice)

    user_choice = input('''
    1. Rock
    2. Paper
    3. Scissors
    4. Quit
    ''')
    
    user_move = choices[user_choice]

    if user_choice not in ("1", "2", "3", "4"):
        print("Invalid choice!")
        continue

    elif user_move == random_comp_choice:
        print("It's a tie !")

    elif user_choice == "1" and random_comp_choice == "scissors" \
            or user_choice == "2" and random_comp_choice == "rock" \
            or user_choice == "3" and random_comp_choice == "paper":
        print("You won !")
        user_score += 1
        tries -= 1

    elif user_choice == "4":
        print("Bye Bye !")
        break
    else:
        print("Computer wins !")
        computer_score += 1
        tries -= 1

    print(f"Your score: {user_score} | Computer score: {computer_score} ")
    print('-' * 40)

print("Game Over !")
print(f"Your score: {user_score} | Computer score: {computer_score} ")
print('-' * 40)

if user_score > computer_score:
    print("You won this game !")

elif user_score < computer_score:
    print("Computer won this game !")

else:
    print("It's a draw !")
