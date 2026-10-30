import pandas as pd
from src.expense_data import load_expense, validate_expenses
from src.expense_analysis import analyze_expenses

from src.expense_analysis import analyze_expenses


# Load the Excel file
expenses = pd.read_csv("data/expenses.csv")


# Perform the analysis
results = analyze_expenses(expenses)


# Display the results
for name, value in results.items():

    print(f"\n{name}:",value)

    