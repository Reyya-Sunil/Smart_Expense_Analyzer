import pandas as pd

from src.expense_analysis import analyze_expenses

from src.Group_Result_Bar import bar_grap_byGroup



# Load the Excel file
expenses = pd.read_csv("data/expenses.csv")


# Perform the analysis
results = analyze_expenses(expenses)

bar_graph=bar_grap_byGroup(expenses)


# Display the results
for name, value in results.items():

    print(f"\n{name}:",value)

    