# Family Expenses Manager
A command-line interface of an expense manager using Python

[Video Demo](https://youtu.be/ZVfqqai0VIc)

---

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the package `tabulate`
```
$ pip install tabulate
```

---

## Usage
Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```

---

## Description
This is a program that allows you to save the family's names, income and expenses.

It also performes a check up so you can the me sum of the income, expenses and check your net balance.


Starting the program takes you to the main menu.

Following the you just input the letter corresponding to the desired action and press enter.

Main menu areas:
- Check Status
- Expenses
- Family

Check status will present:
- Income
- Expenses
- Net Balance

Expenses menu allows the user to:
- Add a new expense, by description and amount
- Edit an existing expense
- Delete an expense
- Check all actual expenses

Family menu allows the user to:
- Add a new family member by first name, last name and salary. Entry date also gets saved
- Edit a member's name and salary
- Delete a member
- Check all members and their salaries

Data is saved even if you close the program.

All data is saved in two csv files:
- family.csv to store family data
- expenses.csv to store expense data

I hope you find it useful.

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Considerations
Only a simple logic of suming salaries and expenses was apllied to explore the concept.

It can be improved in several ways. It can be used to check each person's income and adjust the expenses so in cases where a couple has a big income difference it will be less harsh for who earns less.

Or in a students home, it can be used to divide the monthly expenses equaly.

Also it can be easily updated to check for savings, taking 10% of the income to be family's csv in a new field.

Feel free to give ideas on how I can improve it
