import os
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
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    #Get data from users and transactions db
    transactions_db = db.execute("SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash_db[0]["cash"]

    return render_template("index.html", database = transactions_db, cash = cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        shares = int(shares)

        #If we don't have a symbol
        if not symbol:
            return apology("Must Provide Symbol")
        #If symbol is not found. Use lookup function to check

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol Does Not Exist")

        if shares < 0:
            return apology("Share value not allowed")

        #Transactions db is created
        transaction_value = shares * stock["price"]

        #Get user from session
        user_id = session["user_id"]

        #Get cash from db
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]

        #Checking user balance
        if user_cash < transaction_value:
            return apology("Not enough balance")

        #Update cash and cash DB
        updt_cash = user_cash - transaction_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updt_cash, user_id)

        #Update transaction DB
        date = datetime.now()
        #INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
        db.execute("INSERT INTO transactions (user_id, symbol, price, shares, date) VALUES(?, ?, ?, ?, ?)", user_id, stock["symbol"], stock["price"], shares, date)

        #Display a message for buy successful
        flash("Buy Successful!")

        # Return function
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    transactions_db = db.execute("SELECT * FROM transactions WHERE user_id = :id", id=user_id)
    return render_template("history.html", transactions = transactions_db)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to account"""
    if request.method == "GET":
        return render_template("add.html")

    else:
        new_cash = request.form.get("new_cash")
        new_cash = float(new_cash)

        if not new_cash:
            return apology("You Must Add A Value")

        if new_cash < 1:
            return apology("You Must Provide A Positive Value")

        #Get user from session
        user_id = session["user_id"]

        #Get cash from db
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]

        #Update cash and cash DB
        updt_cash = user_cash + new_cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updt_cash, user_id)

        #Display a message for buy successful
        flash("Cash Added Successfuly!")

        # Return function
        return redirect("/")


@app.route("/withdraw_cash", methods=["GET", "POST"])
@login_required
def withdraw_cash():
    """Withdraw cash from account"""
    if request.method == "GET":
        return render_template("withdraw.html")

    else:
        new_cash = request.form.get("new_cash")
        new_cash = float(new_cash)

        if not new_cash:
            return apology("You Must Add A Value")

        if new_cash < 1:
            return apology("You Must Provide A Positive Value")

        #Get user from session
        user_id = session["user_id"]

        #Get cash from db
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]

        #Update cash and cash DB
        updt_cash = user_cash - new_cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updt_cash, user_id)

        #Display a message for buy successful
        flash("Cash Withdrawn Successfuly!")

        # Return function
        return redirect("/")


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


@app.route("/quote", methods=["GET", "POST"])        ## https://www.youtube.com/watch?v=8rjuV6VvdZI 29min
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")

        #If we don't have a symbol
        if not symbol:
            return apology("Must Provide Symbol")
        #If symbol is not found. Use lookup function to check

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol Does Not Exist")

        return render_template("quoted.html", name = stock["name"], price = stock["price"], symbol = stock["symbol"])


@app.route("/register", methods=["GET", "POST"])#TODO Add limiters to password length etc
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        #If you don't provide username
        if not username:
            return apology("Must Provide Username")
        #If you don't provide password
        if not password:
            return apology("Must Provide Password")
        #If password don't match
        if not confirmation:
            return apology("Must Provide Password Confirmation")
        #If passwords don't match
        if password != confirmation:
            return apology("Passwords Do Not Match")

        #Hash password
        hash = generate_password_hash(password)

        #Add to database https://www.w3schools.com/sql/sql_insert.asp
        try:
            #INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
            #new_user to rememver the session
            new_user = db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash)
        except:
            return apology("Username already exists")

        #Get session user from register
        session["user_id"] = new_user

        # Redirect user to home page
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols_user = db.execute("SELECT symbol FROM transactions WHERE user_id = :id GROUP BY symbol HAVING SUM(shares) > 0", id=user_id)
        #Iterate through the symbols in db
        return render_template("sell.html", symbols = [row["symbol"] for row in symbols_user])

    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        shares = int(shares)

        #If we don't have a symbol
        if not symbol:
            return apology("Must Provide Symbol")
        #If symbol is not found. Use lookup function to check

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol Does Not Exist")

        if shares < 0:
            return apology("Share value not allowed")


        #Transactions db is created
        transaction_value = shares * stock["price"]

        #Get user from session
        user_id = session["user_id"]

        #Get cash from db
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]

        #Select shares to see if you have enough to sell
        user_shares = db.execute("SELECT shares FROM transactions WHERE user_id = :id AND symbol = :symbol GROUP BY symbol", id=user_id, symbol=symbol)
        user_shares_real = user_shares[0]["shares"]

        if shares > user_shares_real:
            return apology("You Do Not Own This Amount Of Shares")

        #Update cash and cash DB
        updt_cash = user_cash + transaction_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updt_cash, user_id)

        #Update transaction DB
        date = datetime.now()
        #INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
        db.execute("INSERT INTO transactions (user_id, symbol, price, shares, date) VALUES(?, ?, ?, ?, ?)", user_id, stock["symbol"], stock["price"], (-1)*shares, date)

        #Display a message for buy successful
        flash("Sell Successful!")

        # Return function
        return redirect("/")
