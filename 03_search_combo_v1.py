"""Search combo v1 - asks user for combo and displays combo info if found"""


import easygui
search_list = []
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
        combo_names = easygui.enterbox("Please search for a combo name "
                                       "(x to exit): ")
        if combo_names == "x":
            break  # Exits loop back to main loop
        else:
            combo_names = combo_names.lower()
            for combo_name, combo_info in combos.items():
                if combo_name.lower() == combo_names:
                    search_list.append(f"Here is the {combo_name} "
                                       f"combo info:\n\n")
                    for key in combo_info:
                        search_list.append(f"{key}: ${combo_info[key]:.2f}\n")
                    search1 = "".join(search_list)
                    easygui.buttonbox(f"{search1}\nWould you like to "
                                      f"change the combo?"
                                      f" (y for yes, n for no): ",
                                      choices=["yes", "no"])
                    search_list.clear()


search()
