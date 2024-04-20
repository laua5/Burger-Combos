# Main Routine v2 - Using a function instead of just a while loop

import easygui

# Main Routine
easygui.msgbox("######### Welcome! ##########")


def main():
    while True:
        choice = easygui.buttonbox(
            "\nWhat would you like to do?\n1: Search combos\n2: Print the"
            " full list\n3: Add combo\n4: Delete Combo\n5: Exit\nPlease enter "
            "your choice: ",
            choices=["search", "print menu", "add combo",
                     "delete combo", "exit"])
        if choice == "search":
            # Search function goes here
            pass  # Placeholder until the search function is added
        elif choice == "print menu":
            # Print menu function goes here
            pass  # Placeholder until the print menu function is added
        elif choice == "add combo":
            # Add function goes here
            pass  # Placeholder until the add function is added
        elif choice == "delete combo":
            # Delete function goes here
            pass  # Placeholder until the delete function is added
        else:
            easygui.msgbox("goodbye")  # Exits the system
            break


main()
