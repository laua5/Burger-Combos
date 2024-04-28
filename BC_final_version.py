"""Burger combo final version
Components added after they have been created and tested, looping added"""

import easygui

# Existing Menu
combos = {
    "Value":
        {"Beef Burger": 5.69, "Fries": 1, "Fizzy Drink": 1},
    "Cheezy":
        {"Cheese Burger": 6.69, "Fries": 1, "Fizzy Drink": 1},
    "Super":
        {"Cheese Burger": 6.69, "Large Fries": 2, "Smoothie": 2},
}


# Number checker function used to check if prices are integers
def number_checker(price):
    try:
        float_price = float(price)
        return float_price > 0
    except ValueError:
        return False


# Function to search for combos
def search():
    while True:
        combo_names = easygui.enterbox("Please search for a combo name "
                                       "(x to exit): ")
        if combo_names == "x":
            break  # Exits loop back to main loop
        else:
            combo_names = combo_names.lower()
            combo_found = False
            for combo_name, combo_info in combos.items():
                if combo_name.lower() == combo_names:
                    search_list.append(f"Here is the {combo_names} "
                                       f"combo info:\n")
                    for key in combo_info:
                        search_list.append(f"{key}: ${combo_info[key]:.2f}\n")
                    search1 = "".join(search_list)
                    combo_found = True
                    change = easygui.buttonbox(f"{search1}\nWould you like to "
                                               f"change the combo?"
                                               " (y for yes, n for no): ",
                                               choices=["yes", "no"])
                    search_list.clear()
                    if change == "no":
                        break
                    else:
                        change_item = easygui.enterbox("Which item would you "
                                                       "like to change?: ")
                        # Check if the entered item exists in the combo
                        keys_to_remove = []
                        for item in combo_info:
                            if item.lower() == change_item.lower():
                                new_item = easygui.enterbox(f"What item would "
                                                            f"you like to "
                                                            f"replace "
                                                            f"{item} with? ")
                                combo_info[new_item] = new_item
                                new_price = easygui.enterbox(f"What is the "
                                                             f"price of "
                                                             f"{new_item}? ")
                                combo_info[new_item] = float(new_price)
                                keys_to_remove.append(item)
                        # Remove the old items from the combo
                        for item in keys_to_remove:
                            combo_info.pop(item)
                        if not keys_to_remove:
                            easygui.msgbox("Item not found.")
            if not combo_found:
                easygui.msgbox("Combo not found.")


# Adding combo function
def add():
    while True:
        the_name = easygui.enterbox("Enter Combo name to add (x to exit): ")
        if the_name == "x":
            break  # Exits loop back to main loop
        # Checks if name(lower and upper case) is already an existing combo
        if the_name.lower() in (name.lower() for name in combos):
            easygui.msgbox(
                "Combo name has already been taken. Please enter another name,"
                " or exit the program.")
            continue
        else:
            while True:
                combos[the_name] = {}
                first_item = easygui.enterbox("Please enter first item to "
                                              "add: ")
                combos[the_name][f'{first_item}'] = first_item
                first_item_price = easygui.enterbox(f"Please enter price of "
                                                    f"{first_item} in dollars "
                                                    f"without $ sign: ")
                # Checks if price is valid
                if not number_checker(first_item_price):
                    easygui.msgbox("Please enter a valid price "
                                   "(a non-negative number).")
                    continue
                first_item_price = float(first_item_price)
                combos[the_name][f'{first_item}'] = first_item_price
                add_more_item = easygui.enterbox("Please enter another item to"
                                                 " add (x to exit): ")
                if add_more_item == "x":
                    break
                else:
                    while True:
                        combos[the_name][f'{add_more_item}'] = add_more_item
                        add_item_price = easygui.enterbox(f"Please enter price"
                                                          f" of "
                                                          f"{add_more_item}: ")
                        # Checks if price is valid
                        if not number_checker(add_item_price):
                            easygui.msgbox("Please enter a valid price "
                                           "(a non-negative number).")
                            continue
                        add_item_price = float(add_item_price)
                        combos[the_name][f'{add_more_item}'] = add_item_price
                        add_more_item = easygui.enterbox("Please enter another"
                                                         " item to add "
                                                         "(x to exit): ")
                        if add_more_item == "x":
                            break
                    break
            # Confirming and showing details
            for combo_name, combo_info in combos.items():
                if combo_name == the_name:
                    confirm_list.append(f"Here is {the_name}'s combo info:\n")
                    for key in combo_info:
                        confirm_list.append(f"{key}: ${combo_info[key]:.2f}\n")
            confirms = "".join(confirm_list)
            confirm = easygui.buttonbox(f"\n{confirms}\nPlease confirm these "
                                        f"details", choices=["yes", "no"])
            confirm_list.clear()
            if confirm == "yes":
                easygui.msgbox(f"Combo {the_name} has been added to menu.")
                break
            else:
                easygui.msgbox("To change details, please go to search combos "
                               "option.To delete combo, please go to delete "
                               "combos option.")
                break


# Prints full combo menu
def print_list():
    easygui.msgbox("Here is the list of combos: ")
    for combo_item, combo_info in combos.items():
        all_combo_info.append(f"\nCombo Name: {combo_item}\n")
        total_cost = 0
        for key in combo_info:
            all_combo_info.append(f"{key}: ${combo_info[key]:.2f}")
            total_cost += combo_info[key]
            total_cost = round(total_cost, 2)
            if combo_item != "1":
                all_combo_info.append("\n")
        all_combo_info.append(f"Total cost for combo {combo_item} is "
                              f"${total_cost:.2f}\n")
    # Joins all strings into one string
    combo_info = "".join(all_combo_info)
    easygui.msgbox(f" ######## FULL MENU OF COMBOS ########\n{combo_info}")


# Deleting a combo from the menu
def delete():
    while True:
        delete_combo = easygui.enterbox("Please enter combo to delete"
                                        "(x to exit): ")
        if delete_combo == "x":
            break  # Exits loop back to main loop
        else:
            combo_found = False  # Used to check if entered combo exists
            for combo_name, combo_info in combos.items():
                if combo_name == delete_combo:
                    confirm_delete = easygui.buttonbox(f"Please confirm delete"
                                                       f" for {delete_combo} "
                                                       f"combo",
                                                       choices=["yes", "no"])
                    if confirm_delete == "yes":
                        combos.pop(delete_combo)
                        easygui.msgbox(f"Combo {delete_combo} has been deleted"
                                       f" from the menu.")
                    combo_found = True
                    break
            if not combo_found:
                easygui.msgbox("Combo not found.")


# Main Routine
easygui.msgbox("######### Welcome! ##########")
while True:
    all_combo_info = []  # List used to display all combo info
    confirm_list = []  # List used in add function to confirm details of combo
    search_list = []  # List used in search function to show combo info
    choice = easygui.buttonbox("\nWhat would you like to do?\n1: Search combos"
                               "\n2: Print the full list\n3: Add combo\n4: "
                               "Delete Combo\n5: Exit\nPlease enter your "
                               "choice: ", choices=["search", "print menu",
                                                    "add combo", "delete combo"
                                                                 "", "exit"])
    # Displays program options
    if choice == "search":
        search()  # Search function to search for different combos
    elif choice == "print menu":
        print_list()  # Prints full combo menu
    elif choice == "add combo":
        add()  # Gives user option to add a new combo
    elif choice == "delete combo":
        delete()  # Delete function to delete a specific combo
    else:
        easygui.msgbox("Goodbye")  # Exits program
        break
