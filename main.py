import pandas as pd

from src.expense_analysis import analyze_expenses

from src.Group_Result_Bar import bar_grap_byGroup
from src.Group_Result_Bar import filter_date



# Load the Excel file
expenses = pd.read_csv("data/expenses.csv")


# Perform the analysis
results = analyze_expenses(expenses)

#bar_graph=bar_grap_byGroup(expenses)   #stop
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")

result =filter_date(expenses,start,end)
print(result)

# Display the results
for name, value in results.items():

    #print(f"\n{name}:",value)   stop
    pass
    