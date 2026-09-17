"""Run with: python -m unittest -v"""

from decimal import Decimal
import unittest
from unittest.mock import patch

from budget_calculator import calculate_budget, parse_amount, read_amount


class BudgetTests(unittest.TestCase):
    def test_surplus(self):
        result = calculate_budget({"Allowance": Decimal("5000")}, {"Rent": Decimal("2500"), "Food": Decimal("1200")})
        self.assertEqual(result, (Decimal("5000"), Decimal("3700"), Decimal("1300")))

    def test_deficit(self):
        self.assertEqual(calculate_budget({"Work": Decimal("100")}, {"Rent": Decimal("150")})[2], Decimal("-50"))

    def test_empty_and_balanced(self):
        self.assertEqual(calculate_budget({}, {}), (Decimal("0"),) * 3)
        self.assertEqual(calculate_budget({"A": Decimal("25")}, {"B": Decimal("25")})[2], Decimal("0"))

    def test_exact_decimal_arithmetic(self):
        self.assertEqual(calculate_budget({"A": Decimal("0.30")}, {"B": Decimal("0.10"), "C": Decimal("0.20")})[2], Decimal("0"))

    def test_valid_input(self):
        for text, expected in [("", "0"), ("  12.50  ", "12.50"), ("0", "0"), ("999999999.99", "999999999.99")]:
            self.assertEqual(parse_amount(text), Decimal(expected))

    def test_invalid_input(self):
        for text in ["-1", "hello", "NaN", "Infinity", "1e3", "1,000", "1.234", "1000000000", "R20"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_amount(text)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["oops", "-2", "12.50"])
    def test_prompt_retries_invalid_input(self, mock_input, mock_print):
        self.assertEqual(read_amount("Food"), Decimal("12.50"))
        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()
