recipes = {
    #  Demo format of storing recipes
    # 1: {
    #     "name": "name of dish",
    #     "type": "type of cusing",
    #     "desc": "description of dish",
    # },
}
id = 0


def add_recipe():
    global id

    print("Add the Recipe")

    id += 1
    name = input("Enter the name of your recipe: ")
    type = input("Enter the type of cusine: ")
    description = input("Enter the description: ")

    recipes[id] = {
        "name": name,
        "type": type,
        "desc": description,
    }

    print("Recipe added successfully.")


def update_recipe():
    print("\n Update the Recipe.")

    try:
        user_choice = int(input("Enter the id to update: "))
        
        if user_choice not in recipes:
            print("Recipe not found.")
            return

        recipe = recipes[user_choice]

        for key, value in recipe.items():
            old_value = value
            new_value = input(f"Enter the new {key}: ")
            recipe[key] = new_value if new_value else old_value

    except ValueError:
        print("Invalid input. Please enter valid id.")


def delete_recipe():
    print("\n Delete the Recipe.")

    try:
        user_choice = int(input("Enter the id to delete: "))
        
        if user_choice not in recipes:
            print("Recipe not found.")
            return

        recheck = input("Are you sure you want to delete (y/n): ")

        if recheck == "y":
            del recipes[user_choice]
            print(f"Recipe at id {user_choice} deleted successfully.")
        else:
            print("Deletion Cancelled.")
    except ValueError:
        print("Invalid input. Please enter valid id.")


def view_recipe():
    for i in recipes:
        print(f"{i}. {recipes[i]}")


def main():
    manager = {
        1: "Add Recipe",
        2: "Update Recipe",
        3: "Delete Recipe",
        4: "View Recipe",
        5: "Exit"
    }
    print("\n*!The Recipe Management App!*\n")
    while True:
        for index, value in manager.items():
            print(f"{index}. {value}")

        try:
            user_choice = int(input("Enter your choice from above: "))
            match user_choice:
                case 1:
                    add_recipe()
                case 2:
                    update_recipe()
                case 3:
                    delete_recipe()
                case 4:
                    view_recipe()
                case 5:
                    print("Exiting the system.")
                    break
                case _:
                    print("Invalid input, please enter number from 1 - 5.")
        except ValueError:
            print("Invalid input, please enter valid choice.")


main()
