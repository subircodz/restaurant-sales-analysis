"""
Analysis and Engineering module for the Restaurant Sales Analysis project.

This module contains functions for:
- Feature Engineering
- Business Analysis
"""

import pandas as pd
from config import PROCESSED_DATA_DIR


def create_attributes(df: pd.DataFrame, findings: list) -> pd.DataFrame:
    '''
    This function creates additional columns to find revenue, day_name, month, weekend and saves a clean dataset

    Args:
        df: Input DataFrame to create additional columns
        findings: To collect business findings
    
    Return:
        df: Returns back a clean df after creating columns and saving
    '''
    df['Revenue'] = df['Quantity'] * df['Price']
    findings.append("Created Revenue Column.")
    df['Day_Name'] = df['Date'].dt.day_name()
    findings.append("Created Day_Name Column.")
    df['Month'] = df['Date'].dt.month
    findings.append("Created Month Column.")
    df["Weekend"] = df["Day_Name"].isin(["Saturday", "Sunday"])
    df["Weekend"] = df["Weekend"].map({
        True: "Yes",
        False: "No"
    })
    findings.append("Created weekend column.")

    # SAVE THE CLEAN DATASET
    clean_file_name = PROCESSED_DATA_DIR / 'cleaned_dataset.csv' 
    df.to_csv(clean_file_name, index=False)
    print(f"[+] CLEAN DATASET SAVED AT: {clean_file_name}")
    print("=" * 70)

    return df


def business_analysis(df: pd.DataFrame, observations: list) -> pd.DataFrame:
    '''
    Helps analysing business KPI's

    Args:
        df: Input Clean DataFrame to analys business KPI's
        observations: Collect the findings for the KPI's to make report

    Return:
        df: Returns the df after analysis is done
    '''

    print("[+] Business Analysis Started...")
    # Total revenue
    revenue_per_order = df['Quantity'] * df['Price']
    tot_revenue = revenue_per_order.sum()
    print(f"[-] Total Revenue:  {tot_revenue:.2f}")
    observations.append(f"Total Revenue: {tot_revenue}")

    # Average Order Value
    total_orders = df['Order_ID'].count()
    average_order_value = tot_revenue / total_orders
    print("[-] Average Order Value: ", average_order_value)
    observations.append(f"Average Order Value: {average_order_value}")

    # Highest Revenue City
    revenue_by_city = df.groupby('City')['Revenue'].sum()
    highest_revenue_by_city = revenue_by_city.idxmax()
    highest_city_revenue = revenue_by_city.max()
    print(f"[-] {highest_revenue_by_city} city has the highest revenue, Rs. {highest_city_revenue}")
    observations.append(f"{highest_revenue_by_city} city has the highest revenue, Rs. {highest_city_revenue}")

    # highest revenue category
    revenue_by_category = df.groupby('Category')['Revenue'].sum()
    highest_revenue_by_category = revenue_by_category.idxmax()
    highest_category_revenue = revenue_by_category.max()
    print(f"[-] {highest_revenue_by_category} category has the highest revenue, Rs {highest_category_revenue}")
    observations.append(f"[+] {highest_revenue_by_category} category has the highest revenue, Rs {highest_category_revenue}")

    # most sold item
    most_sold_item = df.groupby('Food_Item')['Quantity'].sum().idxmax()
    print(f"[-] Most sold food items: {most_sold_item}")
    observations.append(f"Most sold food items: {most_sold_item}")

    # most used payment method
    most_used_payment_method = df.groupby('Payment_Method')['Payment_Method'].value_counts().idxmax()
    print(f"[-] Most used payment method: {most_used_payment_method}")
    observations.append(f"Most used payment method: {most_used_payment_method}")

    # average rating by category
    avg_rating_by_cat = df.groupby('Category')['Customer_Rating'].mean()
    print(f"[-] Average rating by Category:\n {avg_rating_by_cat.to_string()}")
    observations.append(f"Average rating by Category:\n {avg_rating_by_cat.to_string()}")

    # Top 10 revenue orders
    print("=" * 70)
    revenue_by_orders = df.groupby('Food_Item')['Revenue'].sum()
    top10 = revenue_by_orders.nlargest(10)
    formatter = ", ".join(top10.index)
    print(f"[+] Top ten revenue order: \n{formatter}")
    observations.append(f"Top ten revenue order: \n{formatter}")

    # orders by weekdays
    print("=" * 70)
    orders_by_weekdays = df.groupby('Day_Name')['Order_ID'].count()
    print(f"[+] Orders by Weekdays: \n{orders_by_weekdays.to_string()}")
    observations.append(f"Orders by Weekdays: \n{orders_by_weekdays.to_string()}")

    # monthly revenue
    print("=" * 70)
    monthly_revenue = df.groupby('Month')['Revenue'].sum()
    print(f"[+] Monthly Revenue: \n{monthly_revenue.to_string()}")
    observations.append(f"Monthly Revenue: \n{monthly_revenue.to_string()}")

    # highest quantity item
    print("=" * 70)
    highest_qty_item = df.groupby('Food_Item')['Quantity'].sum().idxmax()
    print(f"[+] Highest Quantity Item: {highest_qty_item}")
    observations.append(f"Highest Quantity Item: {highest_qty_item}")

    # revenue by payment method
    print("=" * 70)
    revenue_by_payment_method = df.groupby('Payment_Method')['Revenue'].sum()
    print(f"[-] Revenue by Payment Method: \n{revenue_by_payment_method.to_string()}")
    observations.append(f"Revenue by Payment Method: \n{revenue_by_payment_method.to_string()}")

    # top rated items
    print("=" * 70)
    top5_rated_items = df.groupby('Food_Item')['Customer_Rating'].max().nlargest(5)
    print(f"[-] Top 5 rated items: \n{top5_rated_items.to_string()}")
    observations.append(f"Top 5 rated items: \n{top5_rated_items.to_string()}")

    # lowest performing category, as metric not clear, considering Revenue
    print("=" * 70)
    lowest_perform_cat = df.groupby('Category')['Revenue'].sum().idxmin()
    print(f"[-] Lowest Performing Category by Revenue: {lowest_perform_cat}")
    observations.append(f"[-] Lowest Performing Category by Revenue: {lowest_perform_cat}")

    # city wise average order value
    print("=" * 70)
    revenue_citywise = df.groupby('City')['Revenue'].sum()
    orders_citywise = df.groupby('City')['Order_ID'].count()
    aov_citywise = revenue_citywise / orders_citywise
    print(f"[-] Average Order Value City Wise: \n{aov_citywise:.2f}")
    observations.append(f"Average Order Value City Wise: \n{aov_citywise:.2f}")

    return df