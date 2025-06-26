from currency_converter import CurrencyConverter
from datetime import date


c = CurrencyConverter()

amt = float(input("\nEnter amount in USD: "))

new_amt = c.convert(amt, "USD", "INR", date = date(2023, 6, 26))


print(f"Amount in INR: {new_amt}")