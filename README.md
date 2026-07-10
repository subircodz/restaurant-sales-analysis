# 🍽️ Restaurant Sales Analysis

## 🎯 Business Problem

Restaurants generate thousands of transactions every month, but raw sales data alone does not answer important business questions.

This project analyzes restaurant sales and order data to identify revenue trends, customer ordering behavior, and operational insights that can support better business decisions.

The objective is not simply to analyze data, but to demonstrate how a Data Analyst approaches a real-world business problem from raw data to actionable insights.

---

## 👥 Stakeholder

Primary Stakeholder

Restaurant Owner / Operations Manager

The analysis supports operational and strategic decisions related to sales performance, menu optimization, staffing, and revenue growth.

--- 

## 📌 Business Objectives

The analysis attempts to answer questions such as:

- Which menu categories generate the highest revenue?
- Which products sell the most?
- Which products generate high revenue despite low sales volume?
- What are the busiest days and hours?
- How does weekend performance compare with weekdays?
- Which months perform better?
- Are there opportunities to improve menu pricing or promotions?

## 🗂️ Dataset

The dataset contains restaurant order transactions including:

- Order Date
- Menu Item
- Category
- Quantity
- Unit Price

The dataset is used solely for learning and portfolio purposes.

---

## 🔄 Project Workflow

The project follows a structured analytical workflow.

```
Raw Dataset
      │
      ▼
Data Understanding
      │
      ▼
Data Cleaning
      │
      ▼
Data Validation
      │
      ▼
Feature Engineering
      │
      ▼
Business Analysis
      │
      ▼
Business Findings
```
---

## 🏗️ Project Architecture

```
restaurant-sales-analysis/
├── CHANGELOG.md
├── data
│   ├── processed
│   │   └── cleaned_dataset.csv
│   └── raw
│       └── restaurant_orders.csv
├── LICENSE
├── output
│   ├── charts
│   └── reports
├── README.md
├── requirements.txt
├── Restaurant_Sales_Analysis_Tasks.pptx
└── src
    ├── analysis.py
    ├── config.py
    ├── main.py
    ├── preprocessing.py
    ├── report.py
    └── visualization.py


```

The project follows a modular architecture where each module has a single responsibility.


### 📑 main.py

Acts as the project orchestrator.

It controls the overall analytical workflow without containing business logic.

### 📑 preprocessing.py

Responsible for:

- Loading data
- Exploring the dataset
- Cleaning data
- Validating data

### 📑 analysis.py

Responsible for:

- Feature engineering
- Business analysis
- Business observations

### 📑 report.py

Responsible for:

- Generating business reports and summarizing analytical findings.

### 📑 visualization.py

Responsible for:

- Generating visualizations and KPI dashboards used throughout the analysis.

### 📑 config.py

Responsible for:

- Centralizing project configuration such as file paths, directories, and reusable project settings.

---

## ⚙️ Setup

### Clone the repository

```bash
git clone https://github.com/<your-user-name>/restaurant-sales-analysis.git

cd restaurant-sales-analysis
```
### Install Dependencies
```
pip install -r requirements.txt
```
## ▶️ Run the program
```
python src/main.py
```

## 🔍 Analysis Pipeline

The project follows six analytical phases.

### Phase 1 — Data Understanding

Understand dataset structure, data types, missing values, duplicates, and overall quality.

### Phase 2 — Data Cleaning

Remove inconsistencies and prepare data for analysis.

### Phase 3 — Data Validation

Validate business rules and ensure data quality before analysis.

### Phase 4 — Feature Engineering

Create additional analytical attributes such as:

- Revenue
- Month
- Day Name
- Weekend Indicator

These features make later business analysis easier.

### Phase 5 — Business Analysis

Perform exploratory business analysis to answer stakeholder questions.

### Phase 6 — Business Findings

Summarize observations and business recommendations.

---

## 💡 Key Business Insights

The analysis identified several important observations, including:

- Weekend sales generated higher revenue than weekdays.
- A small number of menu items contributed disproportionately to total revenue.
- Lunch hours consistently produced the highest order volume.
- Beverage sales increased significantly during weekends.

--- 

## 📈 Business Recommendations

- Consider increasing staffing during weekends.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Pathlib

---

## 🎓 Skills Demonstrated

- Data Cleaning
- Data Validation
- Feature Engineering
- Exploratory Data Analysis
- Business Analysis
- Modular Python Programming
- Code Organization
- Business Storytelling

---

## Current Status

Version 1

This project focuses on building a clean analytical workflow.

Future improvements include:

- Interactive dashboard
- Logging
- Unit testing
- Command-line interface

---

## 🎓 Learning Outcomes

This project demonstrates more than data visualization.

It demonstrates a complete analytical thinking process:

Raw Data → Clean Data → Validated Data → Business Insights → Business Recommendations

The emphasis is on building maintainable analytical code rather than producing isolated charts.

---

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

> **Understand the business. Engineer the solution. Communicate the insight.**