"""A small monthly student budget calculator. Uses only Python's standard library."""

from decimal import Decimal
import re


INCOME_CATEGORIES = ("Allowance / family support", "Bursary / scholarship", "Part-time work", "Other income")
EXPENSE_CATEGORIES = (
    "Rent / accommodation", "Groceries", "Transport", "Tuition / study fees",
    "Books / stationery", "Phone / data", "Utilities", "Personal / entertainment",
    "Other expenses",
)
MAX_AMOUNT = Decimal("999999999.99")


def parse_amount(text):
    """Accept blank as zero or a nonnegative amount with at most two decimals."""
    text = text.strip()
    if not text:
        return Decimal("0.00")
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", text):
        raise ValueError("Enter a positive amount or 0, with at most two decimal places (e.g. 1250.50).")
    amount = Decimal(text)
    if amount > MAX_AMOUNT:
        raise ValueError("Enter an amount no greater than 999999999.99.")
    return amount.quantize(Decimal("0.01"))


def read_amount(label):
    """Keep prompting until the user supplies a valid amount."""
    while True:
        try:
            return parse_amount(input(f"  {label} (R): "))
        except ValueError as error:
            print(f"  {error}")


def calculate_budget(income, expenses):
    """Return income total, expense total and balance from Decimal amounts."""
    total_income = sum(income.values(), Decimal("0.00"))
    total_expenses = sum(expenses.values(), Decimal("0.00"))
    return total_income, total_expenses, total_income - total_expenses


def main():
    print("STUDENT BUDGET CALCULATOR")
    print("Monthly amounts in South African rand (ZAR).")
    print("Press Enter for 0. Use a decimal point; omit commas and currency symbols.\n")
    print("INCOME")
    income = {category: read_amount(category) for category in INCOME_CATEGORIES}
    print("\nEXPENSES")
    expenses = {category: read_amount(category) for category in EXPENSE_CATEGORIES}
    total_income, total_expenses, balance = calculate_budget(income, expenses)
    print("\nMONTHLY SUMMARY")
    print("-" * 42)
    for category, amount in expenses.items():
        if amount:
            print(f"{category:<28} R {amount:,.2f}")
    print("-" * 42)
    print(f"Total income:    R {total_income:,.2f}")
    print(f"Total expenses:  R {total_expenses:,.2f}")
    print(f"Remaining:       R {balance:,.2f}")
    if balance > 0:
        print(f"You have R {balance:,.2f} left for the month.")
    elif balance < 0:
        print(f"Your expenses exceed your income by R {abs(balance):,.2f}.")
    else:
        print("Your income and expenses balance exactly.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nCalculator cancelled. No budget data was saved.")
