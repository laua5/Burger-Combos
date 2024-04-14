import easygui

# Main Routine
print("######### Welcome! ##########")

while True:
    choice = easygui.buttonbox(
        "\nWhat would you like to do?\n1: Search combos\n2: Print the"
        " full list\n3: Add combo\n4: Delete Combo\n5: Exit\nPlease enter your "
        "choice: ",
        choices=["search", "print menu", "add combo",
                 "delete combo", "exit"])
    if choice == "search":
        # Search function goes here
    elif choice == "print menu":
        # Print menu function goes here
    elif choice == 3:
        # add function goes here
    elif choice == 4:
        # delete function goes here
    else:
        print("goodbye") # Exits the system
        break