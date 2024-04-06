import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
