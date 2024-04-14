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


def search():
    while True:
        combo_names = easygui.enterbox("Please search for a combo name "
                                       "(x to exit): ")
        if combo_names == "x":
            break
        else:
            combo_found = False
            for combo_name, combo_info in combos.items():
                if combo_name == combo_names:
                    print(f"Here is the {combo_names} combo info:\n")
                    for key in combo_info:
                        print(f"{key}: ${combo_info[key]}")
                    combo_found = True
                    change = easygui.buttonbox("\nWould you like to change "
                                               "the combo?"
                                               " (y for yes, n for no): ",
                                               choices=["yes", "no"])
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
                                new_item = easygui.enterbox(f"What item would you "
                                                            f"like to replace "
                                                            f"{change_item} with? ")
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


def add():
    while True:
        the_name = easygui.enterbox("Enter Combo name to add (x to exit): ")
        if the_name == "x":
            break
        else:
            while True:
                combos[the_name] = {}
                first_item = easygui.enterbox("Please enter first item to "
                                              "add: ")
                combos[the_name][f'{first_item}'] = first_item
                first_item_price = easygui.enterbox(f"Please enter price of "
                                                    f"{first_item}: ")
                first_item_price = float(first_item_price)
                combos[the_name][f'{first_item}'] = first_item_price
                add_more_item = easygui.enterbox("Please enter another item to"
                                                 " add (x to exit): ")
                if add_more_item == "x":
                    break
                else:
                    while True:
                        combos[the_name][f'{add_more_item}'] = add_more_item
                        add_item_price = easygui.enterbox(f"Please enter price "
                                                          f"of {add_more_item}: ")
                        add_item_price = float(add_item_price)
                        combos[the_name][f'{add_more_item}'] = add_item_price
                        add_more_item = easygui.enterbox("Please enter another item to"
                                                         " add (x to exit): ")
                        if add_more_item == "x":
                            break
                    break
            for combo_name, combo_info in combos.items():
                if combo_name == the_name:
                    print(f"Here is the {the_name} combo info:\n")
                    for key in combo_info:
                        print(f"{key}: ${combo_info[key]}")
            confirm = easygui.buttonbox("\nPlease confirm these details",
                                        choices=["yes","no"])
            if confirm == "yes":
                print(f"Combo {the_name} has been added to menu.")
                break
            else:
                print("To change details, please go to search combos option."
                      " To delete combo, please go to delete combos option.")
                break


def print_list():
    easygui.msgbox("Here is the list of combos: ")
    for combo_item, combo_info in combos.items():
        print(f"\nCombo Name: {combo_item}")
        total_cost = 0
        for key in combo_info:
            print(f"{key}: ${combo_info[key]}")
            total_cost += combo_info[key]
            total_cost = round(total_cost, 2)
        print(f"Total cost for combo {combo_item} is ${total_cost}")


# deleting a combo from the menu
def delete():
    while True:
        delete_combo = easygui.enterbox("Please enter combo to delete"
                                        "(x to exit): ")
        if delete_combo == "x":
            break
        else:
            combo_found = False
            for combo_name, combo_info in combos.items():
                if combo_name == delete_combo:
                    confirm_delete = easygui.buttonbox(f"Please confirm delete for "
                                                       f"{delete_combo} combo",choices=["yes","no"])
                    if confirm_delete == "yes":
                        combos.pop(delete_combo)
                        easygui.msgbox(f"Combo {delete_combo} has been deleted from"
                              f" menu.")
                    combo_found = True
                    break
            if not combo_found:
                easygui.msgbox("Combo not found.")


# Main Routine
easygui.msgbox("######### Welcome! ##########")
while True:
    choice = easygui.buttonbox("\nWhat would you like to do?\n1: Search combos\n2: Print the"
          " full list\n3: Add combo\n4: Delete Combo\n5: Exit\nPlease enter your choice: ",
                               choices=["search","print menu","add combo",
                                        "delete combo", "exit"])
    if choice == "search":
        search()
    elif choice == "print menu":
        print_list()
    elif choice == "add combo":
        add()
    elif choice == "delete combo":
        delete()
    else:
        easygui.msgbox("goodbye")
        break
