# Existing Menu
combos = {
    "Value":
        {"Beef Burger": 5.69, "Fries": 1, "Fizzy Drink": 1},
    "Cheezy":
        {"Cheese Burger": 6.69, "Fries": 1, "Fizzy Drink": 1},
    "Super":
        {"Cheese Burger": 6.69, "Large Fries": 2, "Smoothie": 2},
}


def search():
    while True:
        combo_names = input("Please search for a combo name (x to exit): ")
        if combo_names == "x":
            break
        else:
            for combo_name, combo_info in combos.items():
                if combo_name == combo_names:
                    print(f"Here is the {combo_names} combo info:")
                    print(f"{combos[f'{combo_names}']}")
                else:
                    print("Combo not found.")


def add():
    while True:
        the_name = input("Enter Combo name to add (x to exit): ")
        if the_name == "x":
            break
        else:
            while True:
                combos[the_name] = {}
                first_item = input("Please enter first item to add: ")
                combos[the_name][f'{first_item}'] = first_item
                first_item_price = input(f"Please enter price of "
                                         f"{first_item}: ")
                combos[the_name][f'{first_item}'] = first_item_price
                add_more_item = input("Please enter another item to add "
                                      "(x to exit): ")
                if add_more_item == "x":
                    break
                else:
                    while True:
                        combos[the_name][f'{add_more_item}'] = add_more_item
                        add_item_price = input(f"Please enter price of "
                                               f"{add_more_item}: ")
                        combos[the_name][f'{add_more_item}'] = add_item_price
                        add_more_item = input("Please enter another item to"
                                              " add (x to exit): ")
                        if add_more_item == "x":
                            break
                break
        break


def print_list():
    print("Here is the list of combos: ")
    for combo_item, combo_info in combos.items():
        print(f"\nCombo Name: {combo_item}")
        for key in combo_info:
            print(f"{key}: ${combo_info[key]}")


def delete():
    print()


# Number Checking function (based off lucky unicorn)
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number; between {} to {}\n".format(low, high)

    # Keep asking until a valid amount (1 or 2) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))
            if response == "x":
                break
            # check for number within the required range
            elif low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


print("######### Welcome! ##########")
while True:
    print("\nWhat would you like to do?\n1: Search combos list\n2: Print the"
          " full list\n3: Add combo\n4: Delete Combo\n5: Exit")
    choice = num_check("Please enter your choice(number between 1 and 5): ",
                       1, 5)
    if choice == 1:
        search()
    elif choice == 2:
        print_list()
    elif choice == 3:
        add()
    elif choice == 4:
        delete()
    else:
        print("goodbye")
        break
