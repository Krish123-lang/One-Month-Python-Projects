# v1
from decimal import Decimal, InvalidOperation


def display_menu():
    """Display the main banking menu."""
    print("\n" + "=" * 45)
    print("             BANKING SYSTEM")
    print("=" * 45)
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")
    print("=" * 45)


def get_menu_choice():
    """Get a valid menu choice from the user."""

    while True:
        choice = input("Enter your option (1-4): ").strip()

        if choice in {"1", "2", "3", "4"}:
            return choice

        print("Error: Please enter a number between 1 and 4.")


def get_amount(prompt):
    """Get a valid positive monetary amount."""

    while True:
        user_input = input(prompt).strip()

        try:
            amount = Decimal(user_input)

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                continue

            return amount.quantize(Decimal("0.01"))

        except InvalidOperation:
            print("Error: Please enter a valid amount.")


def deposit(balance):
    """Deposit money into the account and return the new balance."""

    amount = get_amount("Enter the amount to deposit: $")

    balance += amount

    print(f"Successfully deposited: ${amount:,.2f}")
    print(f"Current balance: ${balance:,.2f}")

    return balance


def withdraw(balance):
    """Withdraw money from the account and return the new balance."""

    amount = get_amount("Enter the amount to withdraw: $")

    if amount > balance:
        print("Error: Insufficient balance.")
        print(f"Current balance: ${balance:,.2f}")
        return balance

    balance -= amount

    print(f"Successfully withdrawn: ${amount:,.2f}")
    print(f"Current balance: ${balance:,.2f}")

    return balance


def check_balance(balance):
    """Display the current account balance."""

    print(f"Current balance: ${balance:,.2f}")


def main():
    """Run the banking application."""

    balance = Decimal("0.00")

    print("=" * 45)
    print("       Welcome to the Banking System")
    print("=" * 45)

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            balance = withdraw(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            print("\nThank you for using the Banking System.")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
    
    
''' v2
from decimal import Decimal, InvalidOperation


class BankAccount:
    """Represents a simple bank account."""

    def __init__(self, initial_balance=Decimal("0.00")):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self._balance = initial_balance

    @property
    def balance(self):
        """Return the current account balance."""
        return self._balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self._balance:
            raise ValueError("Insufficient balance.")

        self._balance -= amount


def get_amount(prompt):
    """Get and validate a positive monetary amount from the user."""

    while True:
        user_input = input(prompt).strip()

        try:
            amount = Decimal(user_input)

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                continue

            return amount.quantize(Decimal("0.01"))

        except InvalidOperation:
            print("Error: Please enter a valid amount.")


def display_menu():
    """Display the banking menu."""

    print("\n" + "-" * 45)
    print("             BANKING SYSTEM")
    print("-" * 45)
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")
    print("-" * 45)


def display_balance(account):
    """Display the current account balance."""

    print(f"Current balance: ${account.balance:,.2f}")


def handle_withdraw(account):
    """Handle the withdrawal operation."""

    amount = get_amount("Enter the amount to withdraw: $")

    try:
        account.withdraw(amount)
        print(f"Successfully withdrawn: ${amount:,.2f}")
        display_balance(account)

    except ValueError as error:
        print(f"Error: {error}")


def handle_deposit(account):
    """Handle the deposit operation."""

    amount = get_amount("Enter the amount to deposit: $")

    try:
        account.deposit(amount)
        print(f"Successfully deposited: ${amount:,.2f}")
        display_balance(account)

    except ValueError as error:
        print(f"Error: {error}")


def get_menu_choice():
    """Get a valid menu choice from the user."""

    while True:
        choice = input("Enter your option (1-4): ").strip()

        if choice in {"1", "2", "3", "4"}:
            return choice

        print("Error: Please select an option between 1 and 4.")


def main():
    """Run the banking application."""

    account = BankAccount()

    print("=" * 45)
    print("       Welcome to the Banking System")
    print("=" * 45)

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            handle_withdraw(account)

        elif choice == "2":
            handle_deposit(account)

        elif choice == "3":
            display_balance(account)

        elif choice == "4":
            print("\nThank you for using the Banking System.")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

'''
