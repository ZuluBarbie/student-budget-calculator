# Student Budget Calculator

A beginner-friendly Python command-line application for calculating a student's monthly income, expenses, and remaining budget in South African rand (ZAR).

## Features

- Four income categories and nine student expense categories.
- Total income, total expenses, and a surplus, deficit, or balanced result.
- Input validation, including retrying invalid or negative amounts.
- Exact currency arithmetic using Python's `Decimal` type.
- No third-party dependencies. Budget entries stay in the current session and are not saved or uploaded.

## Run

Install Python 3.10 or newer, download or clone this repository, and open a terminal in its folder:

```sh
python budget_calculator.py
```

On Windows, use `py budget_calculator.py` if `python` is unavailable. On macOS/Linux, you may need `python3`.

Enter **monthly** amounts such as `1250.50`. Press Enter to use zero. Omit commas and currency symbols. Each amount may have up to two decimal places and may not exceed `999999999.99`. For fees paid annually or per term, enter your own monthly allocation. Press Ctrl+C to cancel.

For example, enter allowance `5000`, rent `2500`, groceries `1200`, and leave all other categories blank:

```text
Total income:    R 5,000.00
Total expenses:  R 3,700.00
Remaining:       R 1,300.00
You have R 1,300.00 left for the month.
```

## Tests

```sh
python -m unittest -v
```

Tests cover surplus, deficit, balanced and empty budgets, exact decimal arithmetic, valid and invalid amounts, and retrying input.

## Project structure

- `budget_calculator.py`: input, calculation, and summary functions.
- `test_budget_calculator.py`: standard-library unit tests.

This project demonstrates functions, dictionaries, loops, exception handling, input validation, and unit testing.
