# Print menu v2 - building on from v1, by showing total costs of each combo

import easygui
all_combo_info = []

combos = [["Value", "Beef Burger", 5.69, "Fries", 1, "Fizzy Drink", 1],
          ["Cheezy", "Cheese Burger", 6.69, "Fries", 1, "Fizzy Drink", 1],
          ["Super", "Cheese Burger", 6.69, "Fries", 1, "Fizzy Drink", 1]]


# Prints full combo menu
def print_list():
    easygui.msgbox("Here is the list of combos: ")
    for item in combos:
        combo_name = item[0]
        items_prices = item[1:]
        combo_info = []
        total_cost = 0
        for i in range(0, len(items_prices), 2):
            item_name = items_prices[i]
            item_price = items_prices[i + 1]
            combo_info.append(f"{item_name}: ${item_price:.2f}")
            total_cost += item_price
        combo_info = "\n".join(combo_info)
        all_combo_info.append(
            f"Combo {combo_name}:\n{combo_info}\nTotal cost: ${total_cost:.2f}\n\n")
    combo_info = "".join(all_combo_info)
    easygui.msgbox(f" ######## FULL MENU OF COMBOS ########\n{combo_info}")


print_list()
