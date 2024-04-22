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
        total_cost = 0
        for key in combo_info:
            all_combo_info.append(f"{key}: ${combo_info[key]:.2f}")
            total_cost += combo_info[key]
            total_cost = round(total_cost, 2)
            if combo_item != "1":
                all_combo_info.append("\n")
        all_combo_info.append(f"Total cost for combo {combo_item} is "
                              f"${total_cost:.2f}\n")
    combo_info = "".join(all_combo_info)
    easygui.msgbox(f" ######## FULL MENU OF COMBOS ########\n{combo_info}")


print_list()
