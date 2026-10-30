import numpy as np
import pandas as pd

def  validate_expenses(expenses):
    required_columns = ["Date","Category","Amount"]
    if not all(col in expenses.columns for col in required_columns ):
        raise ValueError("Required Columns are Missing")
    return expenses
#calculate toatal expenses
def calculate_total(expenses):
    
    total=np.sum(expenses["Amount"])
    return total
#Calculate average expenses
def calculate_average(expenses):
    average=np.mean(expenses["Amount"])
    return average
#calculate highest expenses
def highest_expenses(expenses):
    highest=np.max(expenses["Amount"])
    return highest
#Calculate lowest expenses
def lowest_expenses(expenses):
    lowest=np.min(expenses["Amount"])
    return lowest
# category wise Expenses  based on the Amount
def Category_wise_expenses(expenses):
    Category_total=expenses.groupby("Category")["Amount"].sum()
    return Category_total

#Daily wise expenses
def daily_expenses(expenses):
    
    expenses["Date"] =pd.to_datetime(expenses["Date"])
    daily_totals=expenses.groupby("Date")["Amount"].sum()
    return daily_totals

def analyze_expenses(expenses):
    
    expenses=validate_expenses(expenses)
    result ={
        "Total Expenses          ":calculate_total(expenses),
        "Average Expenses        ":calculate_average(expenses),
        "Highest Expenses        ":highest_expenses(expenses),
        "Lowest Expenses         ":lowest_expenses(expenses),
        "Category Wise Expenses  ":Category_wise_expenses(expenses),
        "Daily Expenses          ":daily_expenses(expenses)
    }
    return result 
