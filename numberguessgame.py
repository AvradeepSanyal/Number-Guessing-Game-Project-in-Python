import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        print(f"Your guess is:", guess)
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the right number :)")
            break
    except ValueError:
        print("Enter a valid number!")