import random


def generate_random_number(A, B):
    return random.randint(A, B)


def main():
    try:
        start_point = int(input("Select the start point: "))
        end_point = int(input("Select the ending point: "))
        
        guess_limit = 10
        magic_number = generate_random_number(start_point, end_point)

        while True:
            user_input = int(input("\nGuess the number: "))

            if user_input < start_point or user_input > end_point:
                print("Invalid number, please enter number in range.")
                continue

            if user_input == magic_number:
                guess_limit -= 1
                print(f"You guessed the right number in {10 - guess_limit} attempts!")
                break
            elif user_input < magic_number:
                guess_limit -= 1
                print(f"Try Again! You guessed too low, {guess_limit} attempt left.")
            elif user_input > magic_number:
                guess_limit -= 1
                print(f"Try Again! You guessed too high, {guess_limit} attempt left")

            if guess_limit == 0:
                print("Sorry you did not guess the number.!")
                break

    except ValueError:
        print("Invalid Input, please enter valid input.")

main()
