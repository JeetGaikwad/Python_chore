import random


def get_computer_choice():
    return random.randint(1, 3)


def determine_winner(user_choice, computer_choice, user_point, computer_point):
    """
        Based on choice, points are given to the user or computer.
    """
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("Computer wins! Paper covers Rock")
        computer_point += 1
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("User wins! Paper covers Rock")
        user_point += 1
    elif user_choice == "Rock" and computer_choice == "Scissor":
        print("User wins! Rock crushes Scissor")
        user_point += 1
    elif user_choice == "Scissor" and computer_choice == "Rock":
        print("Computer wins! Rock crushes Scissor")
        computer_point += 1
    elif user_choice == "Paper" and computer_choice == "Scissor":
        print("Computer wins! Scissor cuts Paper")
        computer_point += 1
    elif user_choice == "Scissor" and computer_choice == "Paper":
        print("User wins! Scissor cuts Paper")
        user_point += 1

    return user_point, computer_point


def main():
    """
        Main function of the Rock, Paper, Scissor game.
    """
    options = {
        1: "Rock",
        2: "Paper",
        3: "Scissor"
    }
    user_points = 0
    computer_points = 0

    print("Welcome to the Rock, Paper, and Scissor game.")

    while True:

        for index, value in options.items():
            print(f"{index}. {value}")

        try:
            user_input = int(input("Enter your choice (1-3): "))
            if user_input not in options:
                print("Invalid choice! Please select a valid option.")
                continue

            user_choice = options[user_input]
            computer_choice = options[get_computer_choice()]

            print(f"\n You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}\n")

            user_points, computer_points = determine_winner(
                user_choice, computer_choice, user_points, computer_points)

            if user_points == 5:
                print(f"User wins the game by {user_points}-{computer_points}!")
                break
            elif computer_points == 5:
                print(f"Computer wins the game by {computer_points}-{user_points}!")
                break

            # print(result)
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 3.")


main()
