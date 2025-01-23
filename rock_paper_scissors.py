import random


def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("Computer wins! Paper covers Rock")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("User wins! Paper covers Rock")
    elif user_choice == "Rock" and computer_choice == "Scissor":
        print("User wins! Rock crushes Scissor")
    elif user_choice == "Scissor" and computer_choice == "Rock":
        print("Computer wins! Rock crushes Scissor")
    elif user_choice == "Paper" and computer_choice == "Scissor":
        print("Computer wins! Scissor cuts Paper")
    elif user_choice == "Scissor" and computer_choice == "Paper":
        print("User wins! Scissor cuts Paper")
    

def main():
    options = {
        1: "Rock",
        2: "Paper",
        3: "Scissor"
    }
    
    print("Welcome to the Rock, Paper, and Scissor game.")
    for index, value in options.items():
        print(f"{index}. {value}")

    try:
        user_input = int(input("Enter your choice (1-3): "))
        if user_input not in options:
            print("Invalid choice! Please select a valid option.")
            
        user_choice = options[user_input]
        computer_choice = options[get_computer_choice()]
        
        print(f"\n You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        
        result = determine_winner(user_choice, computer_choice)
        
        print(result)
    except ValueError:
        print("Invalid input! Please enter a number from 1 to 3.")


main()
