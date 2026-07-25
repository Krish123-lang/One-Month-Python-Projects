import random


def number_guessing_game():
    max_tries = 3
    while max_tries > 0:
        try:
            random_number = random.randint(1, 10)
            n = int(input("Enter the number: "))
            if n < random_number:
                print("Too low !")

            elif n > random_number:
                print("Too high !")
            else:
                print("Congratulations! That was a perfect shot...")
                return
            max_tries -= 1
            print(f"Tries left: {max_tries}")
        except ValueError:
            print("Invalid Input")

    print(f"Game Over! The valid number was {random_number}")


number_guessing_game()
