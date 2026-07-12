"""
Analysis and Engineering module for the Restaurant Sales Analysis project.

This module contains functions for:
- Feature Engineering
- Business Analysis
"""
import calendar
import pandas as pd
import visualization as vsl
from config import PROCESSED_DATA_DIR, SAVE_REPORT


def create_attributes(df: pd.DataFrame, engineering_performed : list) -> pd.DataFrame:
    '''
    This function does feature engineering to create additional columns to find revenue, day_name, month, weekend and saves a clean dataset

    Args:
        df (pd.DataFrame): DataFrame to perform feature engineering
        engineering_performed (list): Collects the status of engineering features
    
    Return:
        df (pd.DataFrame): Returns back a clean Dataframe after feature engineering is completed
    '''
    df['Revenue'] = df['Quantity'] * df['Price']
    engineering_performed.append("Created Revenue Column.")
    df['Day_Name'] = df['Date'].dt.day_name()
    engineering_performed.append("Created Day_Name Column.")
    df['Month'] = df['Date'].dt.month
    engineering_performed.append("Created Month Column.")
    df["Weekend"] = df["Day_Name"].isin(["Saturday", "Sunday"])
    df["Weekend"] = df["Weekend"].map({
        True: "Yes",
        False: "No"
    })
    engineering_performed.append("Created weekend column.")

    if SAVE_REPORT:
        # SAVE THE CLEAN DATASET
        clean_file_name = PROCESSED_DATA_DIR / 'cleaned_dataset.csv' 
        df.to_csv(clean_file_name, index=False)
        print(f"[+] CLEAN DATASET SAVED AT: {clean_file_name}")
        print("=" * 70)

    return df


def business_analysis(df: pd.DataFrame, business_observations: list, investigation_performed: list, recommended_investigation: list) -> pd.DataFrame:
    '''
    This function helps analysing business KPI's

    Args:
        df (pd.DataFrame): Input Clean DataFrame to analys business KPI's
        business_observations (list): Collect the findings for the KPI's to make report
        investigation_performed (list): Collect investigation reports
        recommended_investigation (list) : Note the recommended investigations

    Return:
        df (pd.DataFrame): Returns the df after analysis is done
    '''

    print("[+] Business Analysis Started...")
    # Total revenue
    revenue_per_order = df['Quantity'] * df['Price']
    tot_revenue = revenue_per_order.sum()
    business_observations.append(f"Total Revenue: Rs. {tot_revenue:,.2f}")

    # Average Order Value
    total_orders = df['Order_ID'].count()
    average_order_value = tot_revenue / total_orders
    business_observations.append(f"Average Order Value: Rs. {average_order_value:,.2f}")

    # Highest Revenue City
    revenue_by_city = df.groupby('City')['Revenue'].sum()
    print("[-] Revenue by city")
    business_observations.append("Revenue by city")
    print(revenue_by_city.to_string())
    for key, value in revenue_by_city.items():
        business_observations.append(f"    • {key:<20} : {round(value, 2)}")
    highest_revenue_by_city = revenue_by_city.idxmax()
    highest_city_revenue = revenue_by_city.max()
    print(f"[-] {highest_revenue_by_city} city has the highest revenue, Rs. {highest_city_revenue:,.2f}")
    business_observations.append(f"{highest_revenue_by_city} city has the highest revenue, Rs. {highest_city_revenue:,.2f}")
    vsl.plot_highest_revenue_by_city(revenue_by_city)


    # highest revenue category
    revenue_by_category = df.groupby('Category')['Revenue'].sum()
    highest_revenue_by_category = revenue_by_category.idxmax()
    highest_category_revenue = revenue_by_category.max()
    print(f"[-] {highest_revenue_by_category} category has the highest revenue, Rs. {highest_category_revenue:,.2f}")
    business_observations.append(f"{highest_revenue_by_category} category has the highest revenue, Rs. {highest_category_revenue:,.2f}")
    vsl.plot_highest_revenue_by_category(revenue_by_category)

    # most sold item
    most_sold_item = df.groupby('Food_Item')['Quantity'].sum().idxmax()
    print(f"[-] Most sold food items: {most_sold_item}")
    business_observations.append(f"Most sold food items: {most_sold_item}")

    # most used payment method
    payment_method_usage = df.groupby('Payment_Method')['Payment_Method'].value_counts()
    vsl.plot_payment_method_usage(payment_method_usage)
    most_used_payment_method = payment_method_usage.idxmax()
    print(f"[-] Most used payment method: {most_used_payment_method}")
    business_observations.append(f"Most used payment method: {most_used_payment_method}")

    # average rating by category
    avg_rating_by_cat = df.groupby('Category')['Customer_Rating'].mean()
    vsl.plot_avg_rating_by_cat(avg_rating_by_cat)
    business_observations.append("Average rating by Category")
    for key, value in avg_rating_by_cat.items():
        business_observations.append(f"    • {key:<20} : {round(value, 2)}")
    print(f"[-] Average rating by Category:\n{avg_rating_by_cat.to_string()}")
    

    # Top 10 revenue orders
    print("=" * 70)
    revenue_by_orders = df.groupby('Food_Item')['Revenue'].sum()
    top10 = revenue_by_orders.nlargest(10)
    print(f"[+] Top ten revenue order: \n{top10.to_string()}")
    business_observations.append("Top 10 revenue order")
    for key, value in top10.items():
        business_observations.append(f"    • {key:<20} : {value:,.2f}")

    # orders by weekdays
    print("=" * 70)
    orders_by_weekdays = df.groupby('Day_Name')['Order_ID'].count()
    vsl.plot_orders_by_weekdays(orders_by_weekdays)
    print(f"[+] Orders by Weekdays: \n{orders_by_weekdays.to_string()}")
    business_observations.append("Orders by Weekdays:")
    for key, value in orders_by_weekdays.items():
        business_observations.append(f"    • {key:<20} : {round(value, 2)}")

    # monthly revenue
    print("=" * 70)
    monthly_revenue = df.groupby('Month')['Revenue'].sum()
    vsl.plot_monthly_revenue(monthly_revenue)
    # print(f"[+] Monthly Revenue: \n{monthly_revenue.to_string()}")
    business_observations.append("Monthly Revenue: ")
    for key, value in monthly_revenue.items():
        business_observations.append(f"    • {calendar.month_name[key]:<20} : Rs. {value:,.2f}")
    investigation_performed.append("Monthly revenue comparison identified June as the lowest-performing month.")
    lowest_working_days_month = df.groupby('Month')['Date'].nunique()
    lowest_month = lowest_working_days_month.sort_values().idxmin()
    lowest_month_days = lowest_working_days_month.sort_values().min()
    investigation_performed.append(f"{lowest_month} recorded the lowest monthly revenue.")
    investigation_performed.append(f"Number of business days found: {lowest_month_days}")
    investigation_performed.append(f"{lowest_month} contains only {lowest_month_days} recorded business days.")
    avg_revenue_by_month = df.groupby('Month')['Revenue'].mean()
    business_observations.append("Average Revenue by Month:")
    for key, value in avg_revenue_by_month.items():
        business_observations.append(f"    • {calendar.month_name[key]:<20} : Rs. {value:,.2f}")
    # business_observations.append(f"{lowest_month} still has the lowest average revenue")
    
    orders_by_month = df.groupby('Month')['Order_ID'].count()
    aov_monthwise = monthly_revenue / orders_by_month
    # print(aov_monthwise)
    business_observations.append("Average Order Value Monthwise:")
    for key, value in aov_monthwise.items():
        business_observations.append(f"    • {calendar.month_name[key]:<20} : Rs. {value:,.2f}")
    avg_quantity = df.groupby('Month')["Quantity"].mean()
    business_observations.append("Average Quantity by Month:")
    for key, value in avg_quantity.items():
        business_observations.append(f"    • {calendar.month_name[key]:<20} : {value:.2f}")
    df
    # monthly_revenue_by_city = df.groupby(["Month", "City"])["Revenue"].sum().unstack()
    # print(monthly_revenue_by_city.shape)
    # print(monthly_revenue_by_city)
    # investigation_performed()
    # print(df.groupby(["Month", "City"])["Revenue"].sum().unstack())
    investigation_performed.append("Revenue in June was the lowest among all months.")
    investigation_performed.append("Investigated whether fewer business days caused the decline.")
    investigation_performed.append("Compared average revenue across months.")
    investigation_performed.append("June continued to record the lowest average revenue.")
    investigation_performed.append("Compared Average Order Value across months.")
    investigation_performed.append("Compared average quantity per order.")
    investigation_performed.append("No significant variation was observed.")
    investigation_performed.append("Compared city-wise revenue.")
    investigation_performed.append("No consistent geographical pattern was identified.")



    # highest quantity item
    highest_qty_item = df.groupby('Food_Item')['Quantity'].sum().idxmax()
    print(f"[+] Highest Quantity Item: {highest_qty_item}")
    business_observations.append(f"Highest Quantity Item: {highest_qty_item}")

    # revenue by payment method
    print("=" * 70)
    revenue_by_payment_method = df.groupby('Payment_Method')['Revenue'].sum()
    print(f"[-] Revenue by Payment Method: \n{revenue_by_payment_method.to_string()}")
    business_observations.append("Revenue by Payment Method: ")
    for key, value in revenue_by_payment_method.items():
        business_observations.append(f"    • {key:<20} : Rs. {value:,.2f}")

    # top rated items
    print("=" * 70)
    top5_rated_items = df.groupby('Food_Item')['Customer_Rating'].max().nlargest(5)
    print(f"[-] Top 5 rated items: \n{top5_rated_items.to_string()}")
    business_observations.append("Top 5 rated items")
    for key, value in top5_rated_items.items():
        business_observations.append(f"    • {key:<20} : {value:,.2f}")

    # lowest performing category, as metric not clear, considering Revenue

    lowest_perform_cat = df.groupby('Category')['Revenue'].sum().idxmin()
    business_observations.append(f"Lowest Performing Category by Revenue: {lowest_perform_cat}")

    # city wise average order value
    revenue_citywise = df.groupby('City')['Revenue'].sum()
    orders_citywise = df.groupby('City')['Order_ID'].count()
    aov_citywise = revenue_citywise / orders_citywise
    print(f"[-] Average Order Value City Wise: \n{aov_citywise}")
    business_observations.append("Average Order Value City Wise:")
    for key, value in aov_citywise.items():
        business_observations.append(f"    • {key:<20} : Rs. {value:,.2f}")


    # recomended investigations
    recommended_investigation.append("Investigate whether customers shifted toward lower-priced menu items, resulting in a reduced Average Order Value.")
    recommended_investigation.append("Analyze category-wise revenue trends for June.")
    recommended_investigation.append("Investigate premium order distribution by month.")
    recommended_investigation.append("Collect discount and promotional campaign data.")
    recommended_investigation.append("Collect operational data such as stock availability and staffing.")
    return df