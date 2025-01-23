import random


def generate_random_number(A, B):
    return random.randint(A, B)


def main():
    start_point = int(input("Select the start point: "))
    end_point = int(input("Select the ending point: "))
    magic_number = generate_random_number(start_point, end_point)

    while True:
        user_input = int(input("\nGuess the number: "))
        if user_input == magic_number:
            print("User guessed the right number!")
            break
        elif user_input < magic_number:
            print("Try Again! You guessed too low.")
        elif user_input > magic_number:
            print("Try Again! You guessed too high.")


main()
