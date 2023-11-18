# Ric Wallet
This project is a web based expense manager using Python and Flask. Previously me and my family relied on excel to input expenses and
use it to divide them in a way that everyone knows ouch much they have to provide, in order to pay the monthly expenses.
Currently I just did the main part of gathering user data and expenses and showing them in the main menu.

## Demonstration
In the following link you can watch a brief demonstration of the app
[Video Demo](https://youtu.be/MexMpKrCz4g)


## Installation
Using CS50's codespace, the user already has all the tools needed. However, in a local machine the user will need several python packages. It is possible that you need some package that I already had. If that happens, python will give you a hint on what you need.

Several commands for packages that are required in order to mimic the CS50's codespace:
```
pip3 install flask

pip3 install flask_session

pip3 install cs50

pip3 install lib50

pip3 install pytz

pip3 install requests

```

---

## Usage
Use flask (https://flask.palletsprojects.com/en/3.0.x/) to run the application
```
$ /path/to/directory/flask run
```
After running the command, a link will be generated and wil allow the user to open the website locally.
---

## Description
This is a program that allows you to save the family members as users. Each user is composed of a username, name, surname and salary. The sum of salaries is visible by all users. Users are able to add expenses. Expenses are composed of a category, description and price. Every user has access to all expenses and is able to delete them. There's also a check status page that allows the user to check the net balance between all salaries and expenses.

The program starts in the login page and after login, the user is taken to the check status page. Then the user can navigate using a navigation bar.


Login menu areas:
- Login
- Register



Naigation Bar:
- Global Status -> Shows salaries, expenses and net balance of all users as a family
- Check expenses -> Shows the expenses of all users
- Add expenses -> Adds a new expense
- Remove expenses -> Deletes existing expense
- Family -> Shows all the user's details
- User -> Shows a menu with details, change password and user delete buttons
- Logout -> Logs out the current account



Global status:
- Family salary total
- Family expense total
- Net balance



Check expenses:
- Expenses for all family member



Add expenses:
- Add an expense by:
-- Category
-- Description
-- Amount



Remove expenses:
- Dropdown with all expenses
- Delete expenses from dropdown



Family:
- For all family members
-- username
-- name
-- surname
-- salary



User:
- User details
- Change password
- Delete user



Logout:
- Logout



Database:
- Transactions table
- Users table




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
