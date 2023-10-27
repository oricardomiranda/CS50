from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        # Prompt user for date of birth in YYYY-MM-DD
        date_birth = input("Date of Birth (YYYY-MM-DD):  ")
        birth_date = date.fromisoformat(date_birth)
        today = date.today()
        delta = today - birth_date
        print(minutes(delta.days))
    except ValueError:
        sys.exit("Invalid Date")

def minutes(days):
    minutes = days * 24 * 60
    return p.number_to_words(minutes, andword= " ").capitalize() + " minutes"

if __name__ == "__main__":
    main()
