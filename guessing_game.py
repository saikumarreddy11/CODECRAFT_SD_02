import random

def guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    while True:
        try:
            # Prompt the user for their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the user's guess with the target number
            if user_guess < target_number:
                print("Too low! Try again.")
            elif user_guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {target_number}.")
                print(f"It took you {attempts} attempts to win the game.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the guessing game
if __name__ == "__main__":
    guessing_game()
