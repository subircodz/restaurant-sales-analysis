"""
Preprocessing module for the Restaurant Sales Analysis project.

This module contains functions for:
- Loading datasets
- Exploring datasets
- Cleaning data
- Data validation

Preprocessing Pipeline

Steps

1. Data Cleaning
2. Validation
3. Feature Engineering
4. Save Clean Dataset

"""

import pandas as pd
from config import RAW_DATA_DIR, DEBUG


# ===============================
# Data Loading
# ===============================
def load_data() -> pd.DataFrame:
    print("[+] Dataset loaded")
    df = pd.read_csv(RAW_DATA_DIR / 'restaurant_orders.csv')
    return df

# ===============================
# Data Exploration
# ===============================
def explore_data(df: pd.DataFrame, data_quality_findings: list) -> None:
    """
    Display an overview of the dataset along with understanding the data within

    Args: 
        df (pd.Dataframe): The dataframe to explore
        data_quality_findings (list): Collects all findings related to data quality 
    """
    if DEBUG:
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
        data_quality_findings.append("There are 181 records, 9 columns")
        data_quality_findings.append("Datatype of Date is wrong")
        data_quality_findings.append("One missing value in Customer_Rating detected")
        data_quality_findings.append("One duplicate record detected")
        data_quality_findings.append("One inconsistent categorical value found")

# ===============================
# Data Cleaning 
# ===============================
def data_cleaning(df: pd.DataFrame, data_corrections: list) -> pd.DataFrame:
    '''
    Clean the data, handle missing value and duplicate records

    Args:
        df (pd.DataFrame): Dataframe to clean and validate
        data_corrections: To collect the findings and observation for reporting
    
    Return:
        df (pd.DataFrame)
    '''
    print("=" * 70)
    print("[+] Cleaning started...")
    df['Date'] = pd.to_datetime(df['Date'])
    data_corrections.append("Corrected the date datatype")
    df['Category'] = df['Category'].replace({
        "Fast food" : "Fast Food"
    })
    data_corrections.append("Corrected the inconsistent categorical value")
    df['Customer_Rating'] = df['Customer_Rating'].fillna(df['Customer_Rating'].mean())
    data_corrections.append("Handled the missing Customer Rating with an average value")
    df = df.drop_duplicates()
    data_corrections.append("Handled the duplicate record")
    print("[+] Cleaning ended...")
    print("=" * 70)
    return df

# ===============================
# Data Validation
# ===============================
def data_validation(df: pd.DataFrame, business_observations: list) -> pd.DataFrame:
    '''
    Data validation for analysing

    Args:
        df (pd.DataFrame): DataFrame for validation
        business_observations (list): Collects business observations
    
    Return:
        df (pd.DataFrame): Returns the DataFrame back after validation
    '''
    print("[+] Validation Started...")
    quantity = df[
        df['Quantity'] <= 0
    ]
    if quantity.empty:
        print("[-] All Quantities seems Valid.")
        business_observations.append("All Quantities seems valid.")
    else:
        print("[!] Invalid Quantity detected.")
        business_observations.append("Invalid Quantity detected.")
        print(quantity)
    price = df[
        df['Price'] <= 0
    ]
    if price.empty:
        print("[-] All Prices seems valid")
        business_observations.append("All Prices seems valid.")
    else:
        print("[!] Invalid Prices detected")
        business_observations.append("Invalid Prices detected.")
        print(price)
    
    ratings = df[
        ~df['Customer_Rating'].between(0, 5)
    ]
    if ratings.empty:
        print("[-] All Ratings are valid.")
        business_observations.append("All Ratings are valid.")
    else:
        print("[!] Invalid ratings detected.")
        business_observations.append("Invalid ratings detected.")
        print(ratings)
    pay_method = df[
        ~df['Payment_Method'].isin(['Cash', 'Card', 'UPI', 'Wallet'])
    ]
    if pay_method.empty:
        print("[-] All Payment methods are valid.")
        business_observations.append("All Payment methods are valid.")
    else:
        print("[!] Invalid Payment method detected.")
        business_observations.append("Invalid Payment method detected.")
        print(pay_method)

    print("[+] Validation ended...")
    print("=" * 70)
    return df