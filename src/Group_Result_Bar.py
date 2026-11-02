import pandas as pd
import matplotlib.pyplot as p
from src.expense_analysis import Category_wise_expenses

def bar_grap_byGroup(expenses):

  total=Category_wise_expenses(expenses)
  colors = [
    "#B71C1C",  # 1. Dark red
    "#E53935",  # 2. Red
    "#F4511E",  # 3. Red-orange
    "#FB8C00",  # 4. Orange
    "#FDD835",  # 5. Yellow
    "#C0CA33",  # 6. Yellow-green
    "#85C244",  # 7. Light green
    "#2E7D32"   # 8. Dark green
  ]

  C_Total=total.sort_values(by="Amount",ascending=False)
  p.bar(total["Category"],total["Amount"],color=colors)
  p.xticks(rotation=45, ha="right")
  p.tight_layout()
  p.title(" Category wise Expenses")
  p.savefig("reports/category_expenses.png", dpi=300, bbox_inches="tight")
