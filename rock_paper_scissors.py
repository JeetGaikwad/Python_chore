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
        computer_point += 1
        print(f"Computer wins! Paper covers Rock, Score Computer {computer_point} User {user_point}")
    elif user_choice == "Paper" and computer_choice == "Rock":
        user_point += 1
        print(f"User wins! Paper covers Rock, Score Computer {computer_point} User {user_point}")
    elif user_choice == "Rock" and computer_choice == "Scissor":
        user_point += 1
        print(f"User wins! Rock crushes Scissor, Computer {computer_point} User {user_point}")
    elif user_choice == "Scissor" and computer_choice == "Rock":
        computer_point += 1
        print(f"Computer wins! Rock crushes Scissor, Computer {computer_point} User {user_point}")
    elif user_choice == "Paper" and computer_choice == "Scissor":
        computer_point += 1
        print(f"Computer wins! Scissor cuts Paper, Computer {computer_point} User {user_point}")
    elif user_choice == "Scissor" and computer_choice == "Paper":
        user_point += 1
        print(f"User wins! Scissor cuts Paper, Computer {computer_point} User {user_point}")

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
    game_round = 0
    while True:

        game_round += 1
        for index, value in options.items():
            print(f"{index}. {value}")

        try:
            print(f"Round {game_round}")
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
                print(f"User wins the game by {user_points}-{computer_points} in {game_round} rounds!")
                break
            elif computer_points == 5:
                print(f"Computer wins the game by {computer_points}-{user_points} in {game_round} rounds!")
                break

            # print(result)
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 3.")


main()
