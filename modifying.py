import random

limit = 3 
best_score = None

def guess(number_to_guess, min, max):
    global best_score
    attempts = 0
    while attempts < limit:
        try:
            guess = int(input(f"Guess the number between {min} and {max}: "))
            print("----------------------------")

            if guess < min or guess > max:
                print("Guessed number cant exceed the range! Try again!")
                print("Dont worry! Your attempt will be resetted to 0")
                print("----------------------------")
                attempts = 0
                continue

            attempts = attempts + 1
            print(f"Attempt no: {attempts}")


            if guess < number_to_guess:
                print("Too low!")
                print("----------------------------")
            elif guess > number_to_guess:
                print("Too high!")
                print("----------------------------")
            else:
                print("Congratulations! You guessed the right number :)")
                print("----------------------------")
                return attempts

            if attempts == limit:
                print(f"Oops! Out of attempts!\nThe correct guess is {number_to_guess}, Better luck next time!")
                print("----------------------------")
                return None
       
        except ValueError:
                print("Enter a valid number!")
                print("----------------------------")

def start_game():
    global best_score
    while True:
        try:
            min = int(input("Enter the minimum range of number you wanna play in: \n"))
            max = int(input("Enter the maximum range of number you wanna play in: \n"))
            print("----------------------------")
            print("Max attempts you will get is 3")
            print("----------------------------")

            if min <= 0 or max <= 0: #corrected lower than EQUAL to 0, otherwise logic didnt understood, if i input min -1 and max 0 it ignores the logic and starts the game
                print("Enter a valid positive range of numbers, not negative or equal!")
                print("----------------------------")
                continue #only works for while or for
            if min >= max:
                print(f"{min} is higher than {max}! Range is impossible \nPlease enter minimum to maximum, not the opposite!")
                print("----------------------------")
                continue

            number_to_guess = random.randint(min, max)
            result = guess(number_to_guess, min, max)

            if result is not None:
                if best_score is None or result < best_score:
                    best_score = result
            if best_score is not None:
                print(f"🏆 Best score so far: {best_score} attempt(s)")
            break

        except ValueError:
            print("Enter a valid number, not any other thing!")
            print("----------------------------")

def choice():
        while True:
                choice = input("Do you want to start (Yes/No): ").lower()
                if choice == 'yes':
                    start_game()
                elif choice == 'no':
                    print("Thanks for playing :) Come back again!")
                    print("----------------------------")
                    exit()
                else:
                    print("Enter Valid Input!")
                    print("----------------------------")
                
            
if __name__ == '__main__':
    choice()