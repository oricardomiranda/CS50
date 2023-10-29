from tabulate import tabulate
import csv
import os
from datetime import date

def main():
    print("\nFamily Expense Manager\n")
    running = True

    while running:
        action = get_action()

        if action == "C":
            # Implement the action for checking status
            pass
        elif action == "S":
            # Implement the action for managing salaries
            pass
        elif action == "E":
            # Implement the action for tracking expenses
            pass
        elif action == "F":
            running = family()  # Check if the user wants to continue
        else:
            running = False
            print("Goodbye!")

def get_action():
    instructions = [
        {"Key": "C", "Action": "Check Status"},
        {"Key": "S", "Action": "Salaries"},
        {"Key": "E", "Action": "Expenses"},
        {"Key": "F", "Action": "Family"},
        {"Key": "Q", "Action": "Quit"}
    ]
    return get_user_choice(instructions)

def get_user_choice(menu):
    while True:
        print(tabulate(menu, headers="keys", tablefmt="rounded_outline"))
        choice = input("Choose one action to proceed: ").strip().upper()
        if choice in [item["Key"] for item in menu]:
            return choice
        print("Invalid action, try again.")

def family():
    instructions = [
        {"Key": "A", "Action": "Add new family member"},
        {"Key": "E", "Action": "Edit a family member's data"},
        {"Key": "F", "Action": "Check a family member's financial data"},
        {"Key": "D", "Action": "Delete a family member"},
        {"Key": "Q", "Action": "Quit to Main Menu"}
    ]

    csv_file = "family.csv"

    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "First Name", "Last Name", "Salary", "Entry Date"])

    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
        family_action = input("Choose one action to proceed: ").strip().upper()

        if family_action == "A":
            # Code for adding a new family member
            print("Registering a new family member")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            salary = input("Enter salary: ")
            entry_date = date.today()

            with open(csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                entry_id = sum(1 for row in reader) + 1

            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([entry_id, first_name, last_name, salary, entry_date])

            print("New family member was created!\n")
        elif family_action == "E":
            # Code for editing a family member's data
            pass
        elif family_action == "F":
            # Code for checking a family member's financial data
            pass
        elif family_action == "D":
            # Code for deleting a family member
            pass
        elif family_action == "Q":
            # Return False to indicate that the user wants to quit the family submenu
            return True
        else:
            print("Invalid action, try again.")
    # After the while loop, you can return True to continue running the main menu
    return True

def function_n():
    pass

if __name__ == "__main__":
    main()
