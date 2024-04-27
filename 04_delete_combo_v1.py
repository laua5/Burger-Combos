# Delete combo v1 - asks for combo to delete, and if combo is not found,
# "combo not found" message is displayed and the user is redirected back to
# page asking for combo to delete. "x" to exit.


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


# Deleting a combo from the menu
def delete():
    while True:
        delete_combo = easygui.enterbox("Please enter combo to delete"
                                        "(x to exit): ")
        if delete_combo == "x":
            break  # Exits loop back to main loop
        else:
            combo_found = False
            for combo_name, combo_info in combos.items():
                if combo_name == delete_combo or delete_combo.lower() in \
                        (name.lower() for name in combos):
                    combo_found = True
                    break
            if not combo_found:
                easygui.msgbox("Combo not found.")


delete()
