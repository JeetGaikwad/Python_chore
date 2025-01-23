def calculate_weight(weight, gravity_relative_to_earth):
    """
    Calculates weight on a celestial body given the gravity relative to Earth.
    """
    return weight * gravity_relative_to_earth


# Infinite loop to allow multiple calculations until the user exits
while True:
    # Input to enter weight in Kilograms
    weight = float(input("Enter your weight in Kilograms: "))

    # Check valid weight
    if weight <= 0:
        print("Please enter a positive number")
        break  # Exit the loop if the weight is invalid

    # Dictionary of Celestial bodies and there relative gravity to earth
    celestial_bodies = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Earth": 1.00,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19,
        "Pluto": 0.06
    }

    # Display a list of celestial bodies
    print("Select the celestial body:")
    for i, planet in enumerate(celestial_bodies, start=1):
        print(f"{i}. {planet}")
    print(f"{len(celestial_bodies) + 1}. Exit")  # Option to exit

    # Get the user's choice from the list
    choice = int(input("Select the option from the list: "))

    # Check exit option
    if choice == 11:
        break
    # Validate user's choice
    elif choice < 1 or choice > len(celestial_bodies):
        print("Invalid Choice")
        break  # Exit the loop

    # Retrieve planet name
    planet = list(celestial_bodies.keys())[choice - 1]

    # Calculate the weight on the selected celestial body
    weight_result = calculate_weight(weight, celestial_bodies[planet])
    
    # Display the calculated weight
    print(f"The calculated weight on {planet} is {weight_result}")
