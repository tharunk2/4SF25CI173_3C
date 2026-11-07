import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("superstore_sales.csv")

# Display first 5 rows
print(df.head())

# Step 2: Data Understanding

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())



# Step 3: Checking Null Values

print("\nNull Values in Each Column:")
print(df.isnull().sum())


# Step 4: Handling Null Values Using Mean Imputation

# Replace missing Sales values with the mean Sales
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

# Replace missing Quantity values with the mean Quantity
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

# Replace missing Profit values with the mean Profit
df["Profit"] = df["Profit"].fillna(df["Profit"].mean())

# Check null values after imputation
print("\nNull Values After Mean Imputation:")
print(df.isnull().sum())



# Step 5: Data Transformation

# Convert Order Date from string to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Year column
df["Year"] = df["Order Date"].dt.year

# Create Month column
df["Month"] = df["Order Date"].dt.month

# Create Month Name column
df["Month Name"] = df["Order Date"].dt.month_name()

# Display the transformed data
print("\nData After Transformation:")
print(df.head())

# Display the new data types
print("\nData Types After Transformation:")
print(df.dtypes)



# Step 6: Insight Generation

# Overall business performance
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

print("\n===== OVERALL BUSINESS INSIGHTS =====")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", round(total_quantity, 0))


# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)

# Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\n===== REGION-WISE SALES =====")
print(region_sales)

# Year-wise Sales
year_sales = df.groupby("Year")["Sales"].sum()

print("\n===== YEAR-WISE SALES =====")
print(year_sales)


# Category-wise Profit
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print("\n===== CATEGORY-WISE PROFIT =====")
print(category_profit)

# Top 10 States by Sales
state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP 10 STATES BY SALES =====")
print(state_sales.head(10))


# Top 5 Sub-Categories by Sales
subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP 5 SUB-CATEGORIES =====")
print(subcategory_sales.head(5))



import pandas as pd
import matplotlib.pyplot as plt

# Step 7: Data Visualization

# Step 7: Data Visualization

import os
os.makedirs("charts", exist_ok=True)


# 1. Category-wise Sales
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.show()
plt.close()


# 2. Region-wise Sales
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/sales_by_region.png")
plt.show()
plt.close()


# 3. Year-wise Sales
year_sales.plot(kind="line", marker="o")
plt.title("Year-wise Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/yearly_sales.png")
plt.show()
plt.close()


# 4. Top 10 States by Sales
state_sales.head(10).sort_values().plot(kind="barh")
plt.title("Top 10 States by Sales")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("charts/top_10_states.png")
plt.show()
plt.close()


# 5. Category-wise Profit
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/profit_by_category.png")
plt.show()
plt.close()