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
            combo_found = False
            for combo_name, combo_info in combos.items():
                if combo_name.lower() == combo_names:
                    search_list.append(f"Here is the {combo_name} "
                                       f"combo info:\n\n")
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
                        item_found = False
                        change_item = easygui.enterbox("Which item would you "
                                                       "like to "
                                                       "change?: ")
                        for key in combo_info:
                            if key == change_item:
                                combo_info.pop(change_item)
                                new_item = easygui.enterbox(f"What item would "
                                                            f"you "
                                                            f"like to replace "
                                                            f"{change_item} "
                                                            f"with? ")
                                combos[combo_names][new_item] = new_item
                                new_price = easygui.enterbox(f"What is the "
                                                             f"price of "
                                                             f"{new_item}? ")
                                new_price = float(new_price)
                                combos[combo_names][new_item] = new_price
                                item_found = True
                                break
                        if not item_found:
                            easygui.msgbox("Item not found.")
            if not combo_found:
                easygui.msgbox("Combo not found.")


search()
