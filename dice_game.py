import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Welcome to the Dice Rolling Simulation")
    while True:
        user_input = int(input("Press 1 to roll the dice and 0 to exit: "))
        if user_input == 1:
            dice_value = roll_dice()
            print(f"Dice rolled to {dice_value}!")
        elif user_input == 0:
            print("Exiting the game..")
            break
        else:
            print("Invalid input, press 1 to roll the dice or 0 to exit\n")


main()
