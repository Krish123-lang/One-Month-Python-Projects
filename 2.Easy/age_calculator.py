''' --- v1 ---
from datetime import date


def age_calculator(birth_date):
    today = date.today()
    # return today

    age = today.year - birth_date.year
    # return age, birth_date.year

    has_not_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    return age - has_not_passed


if __name__ == "__main__":
    print("---Age Calculator---")
    try:
        year = int(input("Enter your birth year: "))
        month = int(input("Enter your birth month: "))
        day = int(input("Enter your birth day: "))

        today = date.today()
        if year < 1 and year > today.year:
            raise ValueError("Invalid birth year")
        if month < 1 and month > 12:
            raise ValueError("Month must be between 1 and 12")

        birthday = date(year, month, day)

        if birthday > today:
            raise ValueError("Error: Birth date cannot be in the future.")

        if age_calculator(birthday) > 120:
            raise ValueError("Please enter a realistic birth date.")

        exact_birthdate = age_calculator(birthday)
        print(f"You are {exact_birthdate} years old !")
    except ValueError:
        print(f"Error: Please enter the valid number for the age.")
'''

# v2
from datetime import date
import calendar


def age_calculator(birth_date):
    today = date.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # If today's day is before the birth day,
    # borrow days from the previous month.
    if days < 0:
        months -= 1

        previous_month = today.month - 1
        previous_year = today.year

        if previous_month == 0:
            previous_month = 12
            previous_year -= 1

        days += calendar.monthrange(previous_year, previous_month)[1]

    # If today's month is before the birth month,
    # borrow a year.
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


if __name__ == "__main__":
    print("--- Age Calculator ---")

    try:
        year = int(input("Enter your birth year: "))
        month = int(input("Enter your birth month (1-12): "))
        day = int(input("Enter your birth day: "))

        today = date.today()

        # Validate year
        if year < 1 or year > today.year:
            raise ValueError("Invalid birth year.")

        # Validate month
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")

        # Validate date
        birthday = date(year, month, day)

        # Birth date cannot be in the future
        if birthday > today:
            raise ValueError("Birth date cannot be in the future.")

        years, months, days = age_calculator(birthday)

        print(
            f"You are {years} years, {months} months and {days} days old."
        )

    except ValueError as error:
        print(f"Error: {error}")
