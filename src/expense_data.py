import numpy as np
from pathlib import Path
import pandas as pd
import csv

BASE_DIR=Path(__file__).resolve().parent.parent
file_path=BASE_DIR/"data"/"expenses.csv"



def load_expense(file_path):
   try:
       with file_path.open("r", newline="", encoding="utf-8") as file:
           ##Used to read the csv file 
            reader =csv.DictReader(file)
           # Check whether the CSV file has column headers
            if reader.fieldnames is None:
              return []
            #Store all the file data into list 
            expenses=list(reader)
    
            return expenses
   except  FileNotFoundError :
       print(f"File Not found in this Path {file_path}") 
       return []
   except OSError as error :
       print(f"Error for reading file {error}")
       return []
#this func will remove all the invalid values and Convert ammount into int  and Date & Category into string format  
def validate_expenses(expenses):
    valid_expenses =[]
    ##Must be Required this column
    required_columns = ["Date","Category","Amount"]
    # Itreate the expenses
    for ex in expenses:
        # If the col are not present in expenses the raise error
        if not all(col in expenses.items for col in required_columns):
            raise ValueError("Required Columns are misssing ")
        # make shallow copy
        expenses=expenses.copy()
        #Remove invalid rows 
        expenses =expenses.dropna(subset=required_columns)
        #convert the Amount into integer
        expenses["Amount"]=pd.to_numeric(expenses["Amount"],errors="coerce")
        #Store Only the Amount which has Finite numbers
        expenses =expenses[np.isfinite(expenses["Amount"])]
        #Convert the Date and Category into String
        expenses =expenses[
            expenses["Date"].astype(str).str.strip().ne("")&expenses["Category"].astype(str).str.strip().ne("")
        ]
        #Remove the None rows from the Amount
        expenses["Amount"]=expenses.dropna(subset=["Amount"])
        # Take only Amount positive 
        expenses["Amount"] =expenses[expenses["Amount"]>=0]
        #Reset_the index 
        expenses=expenses.reset_index(drop=True)
        return expenses

def convert_to_arrays(expenses):
    
    ##Amount was convert into numpy
    amounts = expenses["Amount"].to_numpy(dtype=float)
    ##Category was convert into Numpy
    categories = expenses["Category"].to_numpy()
    ##date was convert into Numpy 
    dates = expenses["Date"].to_numpy()
    
    return amounts, categories, dates

    
        
        
