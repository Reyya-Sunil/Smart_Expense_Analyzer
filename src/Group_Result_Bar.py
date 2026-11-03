import pandas as pd
import matplotlib.pyplot as p
from src.expense_analysis import Category_wise_expenses


def filter_date(expenses,start,end):
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end)

    result = expenses[
        (expenses["Date"] >= start_date) &
        (expenses["Date"] <= end_date)
    ]
    Category_wise_total =result.groupby("Category")["Amount"].sum()
    Category_wise_total = Category_wise_total.reset_index()
    Category_wise_total.columns = ["Category", "Amount"]
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
    C_Total=Category_wise_total.sort_values(by="Amount",ascending=False)
    p.bar(C_Total["Category"],C_Total["Amount"],color=colors[:len(C_Total)])
    p.xticks(rotation=45, ha="right")
    p.tight_layout()
    p.title(f" Category wise Expenses Between {start_date} to {end_date} ")
    
    p.savefig("reports/category_expenses.png", dpi=300, bbox_inches="tight")
    
    
    
    return Category_wise_total
    

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
  p.bar(C_Total["Category"],C_Total["Amount"],color=colors)
  p.xticks(rotation=45, ha="right")
  p.tight_layout()
  p.title(" Category wise Expenses")
  p.savefig("reports/category_expenses.png", dpi=300, bbox_inches="tight")
