shopping_list = []

while True:
    selection = input("""
      Welcome to the shopping list
      Please make a selection from one of the following options:

1. Add an item to the shopping list.
2. Display the shopping list.
3. Display the item count.
4. Display the first item in the shopping list.
5. Display the last item in the shopping list.
6. Clear the shopping list.
7. Exit program.
      Selection:""")
    selection = selection.strip().rstrip(".")

    if selection == "1":
        item = input("Please enter the item you would like to add to the shopping list: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")

    elif selection == "2":
        if shopping_list:
            print("Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("The shopping list is currently empty.")  

    elif selection == "3":
        print(f"There are {len(shopping_list)} items in the shopping list.")

    elif selection == "4":
        if shopping_list:
            print(f"The first item in the shopping list is: {shopping_list[0]}")
        else:
            print("The shopping list is currently empty.")

    elif selection == "5":
        if shopping_list:
            print(f"The last item in the shopping list is: {shopping_list[-1]}")
        else:
            print("The shopping list is currently empty.")

    elif selection == "6":
        shopping_list.clear()
        print("The shopping list has been cleared.")

    elif selection == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid selection. Please enter a number from 1 to 7.")
