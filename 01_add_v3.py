# Add function v3 - allows user to add multiple items instead of just one

import easygui
confirm_list = []

# Existing Menu
combos = {
    "Value":
        {"Beef Burger": 5.69, "Fries": 1, "Fizzy Drink": 1},
    "Cheezy":
        {"Cheese Burger": 6.69, "Fries": 1, "Fizzy Drink": 1},
    "Super":
        {"Cheese Burger": 6.69, "Large Fries": 2, "Smoothie": 2},
}


def number_checker(price):
    try:
        float_price = float(price)
        return float_price > 0
    except ValueError:
        return False


def add():
    while True:
        the_name = easygui.enterbox("Enter Combo name to add (x to exit): ")
        if the_name == "x":
            break  # Exits loop back to main loop
        # Checks if name(lower and upper case) is already an existing combo
        if the_name.lower() in (name.lower() for name in combos):
            easygui.msgbox(
                f"Combo name {the_name} has already been taken. Please enter "
                f"another name, or exit the program.")
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
                        if not number_checker(add_item_price):
                            easygui.msgbox("Please enter a valid price "
                                           "(a non-negative number).")
                            continue
                        add_item_price = float(add_item_price)
                        combos[the_name][f'{add_more_item}'] = add_item_price
                        add_more_item = easygui.enterbox("Please enter another"
                                                         "item to add "
                                                         "(x to exit): ")
                        if add_more_item == "x":
                            break
                    break


add()
easygui.msgbox(combos)
