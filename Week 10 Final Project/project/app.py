import os
import re
import sqlite3
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    # Fetch the username from the database
    username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)

    # Check if username_db is empty
    if not username_db:
        # If the user is not found, log them out and redirect to the home page
        session.clear()
        return redirect("/")

    # Extract username from the first row (assuming there's only one row, as in your previous code)
    username = username_db[0]["username"]

    total_salary_db = db.execute("SELECT salary FROM users")
    total_expenses_db = db.execute("SELECT price FROM expenses")

    total_salary = sum(row["salary"] for row in total_salary_db)
    total_expenses = sum(row["price"] for row in total_expenses_db)
    net_balance = total_salary - total_expenses

    return render_template("index.html", total_salary=total_salary, total_expenses=total_expenses, net_balance=net_balance, username=username)




#--------------------------------------------- EXPENSES ---------------------------------------------

@app.route("/check_expenses", methods=["GET"])
@login_required
def check_expenses():
    if request.method == "GET":
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        expenses_db = db.execute("SELECT * FROM expenses")

        total_expense = sum(row["price"] for row in expenses_db)

        return render_template("check_expenses.html", expenses=expenses_db, total_expense=total_expense, username=username)


@app.route("/add_expenses", methods=["GET", "POST"])
@login_required
def add_expenses():
    if request.method == "GET":
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]
        return render_template("add_expenses.html", username=username)
    else:
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        category = request.form.get("category")
        description = request.form.get("description")
        price = request.form.get("price")
        price = float(price)

        # If we don't have a symbol
        if not category:
            return apology("Must Select Category")

        if not description:
            return apology("Must Add Description")

        if price < 0:
            return apology("Price value not allowed")

        # Get user from session
        user_id = session["user_id"]

        # Update transaction DB
        db.execute("INSERT INTO expenses (user_id, category, description, price) VALUES(?, ?, ?, ?)", user_id, category, description, price)

        # Display a message for the successful expense addition
        flash("Expense Added Successfully!")

        # Redirect to the home page
        return redirect("/index.html")



@app.route("/remove_expenses", methods=["GET", "POST"])
@login_required
def remove_expenses():
    if request.method == "GET":
        user_id = session["user_id"]
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        expenses_db = db.execute("SELECT id, description,price FROM expenses")

        return render_template("remove_expenses.html", expenses=expenses_db, username=username)
    else:
        user_id = session["user_id"]

        expense_id = request.form.get("expense_id")
        #If we don't have a symbol
        if not expense_id :
            return apology("Must Select Expense")

        #Update transaction DB
        db.execute("DELETE FROM expenses WHERE id = ?", expense_id)

        #Display a message for buy successful
        flash("Expense Removed Successfully!")

        # Return function
        return redirect("/")


#-----------------------------------------------REGISTER AND LOGIN-----------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        name = request.form.get("name")
        surname = request.form.get("surname")
        salary = request.form.get("salary")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        #If you don't provide username, password or confirmation
        if any(not field for field in [username, name, surname, password, confirmation]):
            return apology("Fields cannot be empty")
        #Username
        if len(username) < 4:
            return apology("Username must have more than 4 characters")
        if not username.isalnum():
            return apology("Username must have characters and numbers only")
        #Password
        if len(password) < 8:
            return apology("Password must have more than 8 characters")
        if (
            not re.search("[a-zA-Z]", password)
            or not re.search("[0-9]", password)
            or not re.search("[!@#$%^&*()]", password)
        ):
            return apology("Password must contain characters, digits and symbols!")
        #If passwords don't match
        if password != confirmation:
            return apology("Passwords Do Not Match")

        #Add to database https://www.w3schools.com/sql/sql_insert.asp
        try:
            #INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
            #new_user to rememver the session
            new_user = db.execute("INSERT INTO users(username, name, surname, salary, hash) VALUES(?,?,?,?,?)", username, name, surname, salary, generate_password_hash(password))
        except:
            return apology("Username already exists")

        flash("Registered Successfully!")

        #Get session user from register
        session["user_id"] = new_user

        # Redirect user to home page
        return redirect("/login")


@app.route("/check_family", methods=["GET"])
@login_required
def check_family():
    if request.method == "GET":
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        family_db = db.execute("SELECT username, name, surname, salary FROM users")

        return render_template("check_family.html", family_db=family_db, username=username)


#-------------------------------------------USER----------------------------------------------------
@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change password"""
    if request.method == "GET":
        # Fetch the username from the database
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        # Render the template with the username
        return render_template("change_password.html", username=username)
    else:
        user_id = session["user_id"]
        password = request.form.get("password")
        new_password = request.form.get("new_password")
        new_confirmation = request.form.get("new_confirmation")

        # If you don't provide username, password, or confirmation
        if any(not field for field in [password, new_password, new_confirmation]):
            return apology("Fields cannot be empty")
        # Password
        if len(new_password) < 8:
            return apology("Password must have more than 8 characters")
        if (
            not re.search("[a-zA-Z]", password)
            or not re.search("[0-9]", password)
            or not re.search("[!@#$%^&*()]", password)
        ):
            return apology("Password must contain characters, digits, and symbols!")
        # If passwords don't match
        if new_password != new_confirmation:
            return apology("Passwords Do Not Match")

        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        # Check password matches db
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("Wrong password!")

        # Update in the database https://www.w3schools.com/sql/sql_insert.asp
        try:
            db.execute("UPDATE users SET hash = (?) WHERE id = (?);", generate_password_hash(new_password), user_id)
        except:
            return apology("Please try again")

        flash("Password updated successfully!")

        # Redirect user to home page
        return redirect("/")


@app.route("/user")
@login_required
def user():
    user_id = session["user_id"]

    # Retrieve the username from the database
    username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    username = username_db[0]["username"]

    return render_template("user.html", username=username)


@app.route("/user_details", methods=["GET"])
@login_required
def user_details():
    if request.method == "GET":
        user_id = session["user_id"]
        user_details_db = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        if not user_details_db:
            return apology("User not found", 404)

        user_id = user_details_db[0]["id"]
        username = user_details_db[0]["username"]
        name = user_details_db[0]["name"]
        surname = user_details_db[0]["surname"]
        salary = user_details_db[0]["salary"]

        return render_template("user_details.html", user_id=user_id, username=username, name=name, surname=surname, salary=salary)


@app.route("/delete_user", methods=["GET", "POST"])
@login_required
def delete_user():
    if request.method == "GET":
        # Fetch the username from the database
        user_id = session["user_id"]
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        # Render the template with the username
        return render_template("delete_user.html", username=username)
    else:
        user_id = session["user_id"]
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)
        username = username_db[0]["username"]

        # If you don't provide password or confirmation
        if not password or not confirmation:
            return apology("Password and confirmation cannot be empty")

        # If passwords don't match
        if password != confirmation:
            return apology("Passwords Do Not Match")

        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        # Check password matches db
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("Wrong password!")

        # Update in the database
        try:
            db.execute("DELETE FROM users WHERE id = ?", user_id)
        except:
            return apology("Please try again")

        if not username_db:
            session.clear()

        # Redirect user to home page
        return redirect("/")
