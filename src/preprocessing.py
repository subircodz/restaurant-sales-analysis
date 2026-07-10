"""
Preprocessing module for the Restaurant Sales Analysis project.

This module contains functions for:
- Loading datasets
- Exploring datasets
- Cleaning data
- Data validation
"""

import pandas as pd
from config import RAW_DATA_DIR


# ===============================
# Data Loading
# ===============================
def load_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_DATA_DIR / 'restaurant_orders.csv')
    return df

# ===============================
# Data Exploration
# ===============================
def explore_data(df: pd.DataFrame, findings: list) -> None:
    """
    Display an overview of the dataset along with understanding the data within

    Args: 
        df: The dataframe to explore
    """
    print("=" * 95)
    print(df.head())
    print("=" * 95)
    print(df.tail())
    print("=" * 95)
    print(df.shape)
    print("=" * 70)
    print(df.dtypes)
    print("=" * 70)
    print(df.columns)
    print("=" * 70)
    print(df.describe())
    print("=" * 70)
    df.info()
    print("=" * 70)
    print("CHECK MISSING VALUE")
    print("=" * 70)
    print(df.isna().sum())
    print("=" * 70)
    print("CHECK DUPLICATE RECORDS")
    print("=" * 70)
    df['Order_ID'] = df['Order_ID'].str.upper()
    print(df.duplicated().sum())
    print("=" * 70)
    print(df['City'].unique())
    print("=" * 70)
    print(df['Food_Item'].unique())
    print("=" * 70)
    print(df['Category'].unique())
    print("=" * 70)
    print(df['Category'].value_counts())
    findings.append("There are 181 records, 9 columns")
    findings.append("Datatype of Date is wrong")
    findings.append("One missing value in Customer_Rating detected")
    findings.append("One duplicate record detected")
    findings.append("One inconsistent categorical value found")

# ===============================
# Data Cleaning 
# ===============================
def data_cleaning(df: pd.DataFrame, findings: list) -> pd.DataFrame:
    '''
    Clean the data, handle missing value and duplicate records

    Args:
        df: Input Pandas Dataframe to clean and validate
        findings: To collect the findings and observation for reporting
    
    Return:
        df: Pandas DataFrame
    '''
    print("=" * 70)
    print("[+] Cleaning started...")
    df['Date'] = pd.to_datetime(df['Date'])
    findings.append("Corrected the date datatype")
    df['Category'] = df['Category'].replace({
        "Fast food" : "Fast Food"
    })
    findings.append("Corrected the inconsistent categorical value")
    df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].mean())
    findings.append("Handled the missing Customer Rating with an average value")
    df = df.drop_duplicates()
    findings.append("Handled the duplicate record")
    print("[+] Cleaning ended...")
    print("=" * 70)
    return df

# ===============================
# Data Validation
# ===============================
def data_validation(df: pd.DataFrame, findings: list) -> pd.DataFrame:
    '''
    Data validation for analysing

    Args:
        df: Input DataFrame for validation
        findings: To collect any anomalies for reporting
    
    Return:
        df: Returns the DataFrame back after validation
    '''
    print("[+] Validation Started...")
    quantity = df[
        df['Quantity'] <= 0
    ]
    if quantity.empty:
        print("[-] All Quantities seems Valid.")
    else:
        print("[!] Invalid Quantity detected.")
        print(quantity)
    price = df[
        df['Price'] <= 0
    ]
    if price.empty:
        print("[-] All Prices seems valid")
    else:
        print("[!] Invalid Prices detected")
        print(price)
    
    ratings = df[
        ~df['Customer_Rating'].between(0, 5)
    ]
    if ratings.empty:
        print("[-] All Ratings are valid.")
    else:
        print("[!] Invalid ratings detected.")
        print(ratings)
    pay_method = df[
        ~df['Payment_Method'].isin(['Cash', 'Card', 'UPI', 'Wallet'])
    ]
    if pay_method.empty:
        print("[-] All Payment methods are valid.")
    else:
        print("[!] Invalid Payment method detected.")
        print(pay_method)

    print("[+] Validation ended...")
    print("=" * 70)
    return df


if __name__ == "__main__":
    findings = []
    df = load_data()
    explore_data(df, findings)
    df = data_cleaning(df, findings)
    df = data_validation(df, findings)