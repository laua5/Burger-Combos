# print menu v3 - using dictionaries, shows basic information of each combo

import easygui
all_combo_info = []  # List used to display all combo info

# Existing Menu
combos = {
    "Value":
        {"Beef Burger": 5.69, "Fries": 1, "Fizzy Drink": 1},
    "Cheezy":
        {"Cheese Burger": 6.69, "Fries": 1, "Fizzy Drink": 1},
    "Super":
        {"Cheese Burger": 6.69, "Large Fries": 2, "Smoothie": 2},
}


# Prints full combo menu
def print_list():
    easygui.msgbox("Here is the list of combos: ")
    for combo_item, combo_info in combos.items():
        all_combo_info.append(f"\nCombo Name: {combo_item}\n")
        for key in combo_info:
            all_combo_info.append(f"{key}: ${combo_info[key]:.2f}\n")
    combo_info = "".join(all_combo_info)
    easygui.msgbox(f" ######## FULL MENU OF COMBOS ########\n{combo_info}")


print_list()
