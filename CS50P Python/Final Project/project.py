from tabulate import tabulate
import csv
import os
from datetime import date

def main():
    print("\nFamily Expense Manager\n")
    running = True

    while running:
        action = main_menu()

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

def main_menu():
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
            add_family_member(csv_file)
        elif family_action == "E":
            # Code for editing a family member's data
            edit_family_member(csv_file)
        elif family_action == "F":
            # Code for checking a family member's financial data
            check_family_member(csv_file)
        elif family_action == "D":
            # Code for deleting a family member
            delete_family_member(csv_file)
        elif family_action == "Q":
            # Return False to indicate that the user wants to quit the family submenu
            return True
        else:
            print("Invalid action, try again.")
    # After the while loop, you can return True to continue running the main menu
    return True


def add_family_member(csv_file):
    print("Registering a new family member")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    salary = input("Enter salary: ")
    entry_date = date.today()

    # Check if the file exists or is empty
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "First Name", "Last Name", "Salary", "Entry Date"])
        entry_id = 1
    else:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            entry_id = sum(1 for row in reader) + 1

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([entry_id, first_name, last_name, salary, entry_date])

    print("New family member was created!\n")


def edit_family_member(csv_file):
    with open(csv_file, mode='r') as file:
        reader = list(csv.DictReader(file))
        # Checking if we have family members
        if not reader:
            print("There are no family members")
            return

        selected_member_id = select_family_member_id(reader)


        if select_family_member_id == 0:
            print("Update canceled.")
            return

        selected_member = reader[selected_member_id - 1]

        updated_first_name = input(f"Enter new first name for {selected_member['First Name']}: ")
        updated_last_name = input(f"Enter new last name for {selected_member['Last Name']}: ")
        updated_salary = input(f"Enter new salary for {selected_member['Salary']}: ")

        selected_member['First Name'] = updated_first_name
        selected_member['Last Name'] = updated_last_name
        selected_member['Salary'] = updated_salary

        with open(csv_file, mode='w', newline='') as file:
            fieldnames = ["ID", "First Name", "Last Name", "Salary", "Entry Date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)

        print("Family member updated.")

def check_family_member(csv_file):
    with open(csv_file, mode='r') as file:
        reader = list(csv.DictReader(file))
        # Checking if we have family members
        if not reader:
            print("There are no family members")
            return

        selected_member_id = select_family_member_id(reader)

        if select_family_member_id == 0:
            print("Check canceled.")
            return

        selected_member = reader[selected_member_id - 1]

        print(tabulate([selected_member], headers="keys", tablefmt="rounded_outline"))
        return


"""def delete_family_member(csv_file):
    with open(csv_file, mode='r') as file:
    reader = list(csv.DictReader(file))
    # Checking if we have family members
    if not reader:
        print("There are no family members")
        return

    selected_member_id = select_family_member_id(reader)

    if select_family_member_id == 0:
        print("Check canceled.")
        return

    selected_member = reader[selected_member_id - 1]

    print("Selected family member to delete:")
    print(tabulate([selected_member], headers="keys", tablefmt="rounded_outline"))

    confirmation =
    return"""


def select_family_member_id(family_data):
    print("Select a family member:")
    print(tabulate(family_data, headers="keys", tablefmt="rounded_outline"))

    while True:
        try:
            selection = int(input("Select a member's ID (or 0 to cancel): "))
            if 0 <= selection <= len(family_data):
                return selection
            print("Invalid ID. Please select a valid ID or 0 to cancel.")
        except ValueError:
            print("Invalid ID. Please enter a number or 0 to cancel.")

    return 0


if __name__ == "__main__":
    main()
