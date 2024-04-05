import random

def guess_the_number(min_value=1, max_value=20):
    # Generate a random number between min_value and max_value
    secret_number = random.randint(min_value, max_value)
    attempts = 0
    max_attempts = int((max_value - min_value) * 0.6) + 1

    print(f"Welcome to Guess the Number Game! I am thinking a number between {min_value} and {max_value}. Can you guess it?")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print(f"Too low! Try again. You have {max_attempts - attempts} attempts left.")
            elif guess > secret_number:
                print(f"Too high! Try again. You have {max_attempts - attempts} attempts left.")
            else:
                print(
                    f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!"
                )
                return
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Sorry, you've run out of attempts! The correct number was {secret_number}.")

if __name__ == "__main__":
    min_value = int(input("Enter the minimum value for the range (default is 1): ") or 1)
    max_value = int(input("Enter the maximum value for the range (default is 20): ") or 20)
    guess_the_number(min_value, max_value)
