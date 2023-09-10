# Initialize an empty shopping list
shopping_list = []

# Function to add an item to the shopping list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

# Function to view the shopping list
def view_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is empty.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add an item to the shopping list")
    print("2. Remove an item from the shopping list")
    print("3. View the shopping list")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        item = input("Enter the item you want to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item you want to remove: ")
        remove_item(item)
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Thank you for using the shopping list program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
