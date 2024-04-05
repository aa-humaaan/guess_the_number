import random

def guess_the_number():
    while True:
        try:
            min_value = int(input("Enter the minimum value for the range (should be between 1 and 10): "))
            if min_value < 1 or min_value > 10:
                print("Invalid input! Please enter a number between 1 and 10.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    while True:
        try:
            max_value = int(input(f"Enter the maximum value for the range (should be greater than {min_value} and less than or equal to 20): "))
            if max_value <= min_value or max_value > 20:
                print(f"Invalid input! Please enter a number greater than {min_value} and less than or equal to 20.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Generate a random number between min_value and max_value
    secret_number = random.randint(min_value, max_value)
    attempts = 0
    max_attempts = int((max_value - min_value) * 0.6) + 1

    print(f"Welcome to Guess the Number Game! I am thinking a number between {min_value} and {max_value}. Can you guess it?")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess (should be between {min_value} and {max_value}): "))
            attempts += 1

            if guess <= min_value:
                print("Please enter a number greater than the minimum value.")
            elif guess > max_value:
                print(f"Please enter a number less than or equal to {max_value}.")
            elif guess < secret_number:
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
    guess_the_number()
