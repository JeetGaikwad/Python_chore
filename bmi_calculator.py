def calculate_bmi(weight, height):
    """Calculates the Body Mass Index (BMI) given weight and height."""
    return weight / height**2


def main():
    """Main function for the BMI calculator."""
    print("Welcome to Body Mass Index (BMI) Calculator!\n")
    try:
        user_name = input("Please enter your name: ")
        user_weight = float(input("Enter your weight in Kilograms (kg): "))
        user_height = float(input("Enter your height in meters (m): "))

    except ValueError:
        print("Invalid input, please enter valid values")
        return

    bmi = calculate_bmi(user_weight, user_height)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        status = "Normal"
    elif bmi >= 25 and bmi < 30:
        status = "Overweight"
    elif bmi >= 30:
        status = "Obesity"

    print(f"{user_name}, your BMI is {bmi:.2f} which is categorized as {status}")


main()
