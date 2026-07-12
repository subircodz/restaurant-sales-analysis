"""
Visualization module to create chart

This module helps to create charts according to business KPI metrics

- Bar Chart
- Scatterplot
"""

import matplotlib.pyplot as plt
import pandas as pd
from config import CHART_DIR, SHOW_CHARTS, SAVE_CHARTS

#===============================
# Decorates the chart
#===============================
def chart_helper(title: str, fname: str) -> None:
    """
    Apply common chart formatting and save the figure.

    This helper applies chart title, axis labels, legend,
    grid, layout adjustments, saves the chart, and closes
    the figure.

    Args:
        title   : Input title to place a title on the chart
        fname   : Input fname to save the save with fname
    """
    plt.title(title)    
    plt.tight_layout()
    if SAVE_CHARTS:
        plt.savefig(CHART_DIR / fname, bbox_inches="tight", dpi=300)
    if SHOW_CHARTS:
        plt.show()
    else:
        plt.close()
    return None

def decorate_chart(x: str, y: str, rotate: float, show_legend: bool = True):
    """
    Apply common bar chart formatting.

    This helper applies axis labels, legend,
    grid, layout adjustments to the bar charts

    Args:
        x       : Input x for labelling x axis
        y       : Input y for labelling y axis
        rotate  : Input rotate for rotating the tick labels
    """
    plt.xlabel(x)
    plt.ylabel(y)
    if show_legend:
        plt.legend(loc="best")
    plt.xticks(rotation = rotate)
    plt.grid(alpha=0.5)
    return None

#=============================================
# Create bar chart for highest revenue city
#=============================================

def plot_highest_revenue_by_city(revenue_by_city: pd.Series) -> None:
    """
    Create and save a bar chart showing total revenue by city.

    Args:
        revenue_by_city: Input the Pandas Series to plot the bar chart
    """
    city = revenue_by_city.index
    revenue = revenue_by_city.values
    plt.figure(figsize=(8,5))
    plt.bar(
        x=city,
        height=revenue,
        label = "Cities",
        edgecolor = "black"
    )
    decorate_chart(x="City", y="Revenue", rotate=45)
    chart_helper(title="Revenue By City", fname="revenue_by_city.png")
    return None



#=============================================
# Create bar chart for highest revenue category
#=============================================

def plot_highest_revenue_by_category(revenue_by_category: pd.Series) -> None:
    """
    Create and save a bar chart showing highest revenue by category.

    Args:
        revenue_by_category: Input the Pandas Series to plot the bar chart
    """
    category = revenue_by_category.index
    revenue = revenue_by_category.values
    plt.figure(figsize=(8,5))
    plt.bar(
        x=category,
        height=revenue,
        label = "Dish Category",
        edgecolor = "black"
    )
    decorate_chart(x="Category", y="Revenue", rotate=45)
    chart_helper(title="Revenue By Category", fname="revenue_by_category.png")
    return None

#=============================================
# Create bar chart for orders by weekdays
#=============================================

def plot_orders_by_weekdays(orders_by_weekdays: pd.Series) -> None:
    """
    Create and save a bar chart showing orders by weekdays.

    Args:
        revenue_by_category: Input the Pandas Series to plot the bar chart
    """
    weekdays = orders_by_weekdays.index
    orders = orders_by_weekdays.values
    plt.figure(figsize=(8,5))
    plt.bar(
        x=weekdays,
        height=orders,
        label = "Weekdays",
        edgecolor = "black"
    )
    decorate_chart(x="Weekdays", y="Orders", rotate=45)
    chart_helper(title="Orders by weekdays", fname="orders_by_weekdays.png")
    return None

#=============================================
# Create bar chart for average ratings by category
#=============================================

def plot_avg_rating_by_cat(avg_rating_by_cat: pd.Series) -> None:
    """
    Create and save a bar chart showing orders by weekdays.

    Args:
        revenue_by_category: Input the Pandas Series to plot the bar chart
    """
    category = avg_rating_by_cat.index
    avg_rating = avg_rating_by_cat.values
    plt.figure(figsize=(8,5))
    plt.bar(
        x=category,
        height=avg_rating,
        label = "Dish Category",
        edgecolor = "black"
    )
    decorate_chart(x="Category", y="Average Rating", rotate=45)
    chart_helper(title="Average Ratings by Dish Category", fname="avg_rating_by_category.png")
    return None

def plot_payment_method_usage(payment_method_usage: pd.Series) -> None:
    """
    Generate pie chart to show most used payment method

    Args:
        payment_method_usage: pd.Series -> Input payment methods usage series to plot pie chart
    """
    payment_methods = payment_method_usage.index
    usage = payment_method_usage.values
    plt.pie(
        x=usage,
        labels=payment_methods,
        autopct="%1.1f%%"
    )
    chart_helper(title="Most used Payment Method", fname="most_used_payment_method.png")
    return


def plot_monthly_revenue(monthly_revenue: pd.Series) -> None:
    month = monthly_revenue.index
    revenue = monthly_revenue.values
    
    plt.plot(
        month,
        revenue,
        marker="o",
        markersize = 6,
        markerfacecolor = "yellow",
    )
    decorate_chart(x="Month", y="Revenue", rotate=45, show_legend=False)
    chart_helper(title="Monthly Revenue", fname="monthly_revenue.png")
    plt.show()
    return None