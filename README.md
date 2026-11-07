# Python Fundamentals Challenge – Milestone 1

## Student Details

- **USN:** 4SF25CI173
- **Section:** 3C

## Project Title

**Sales Data Analysis Using Python and Pandas**

## Objective

The objective of this project is to perform data transformation, handle missing values, generate meaningful insights, and visualize sales data using Python.

## Dataset

The project uses a Superstore Sales dataset containing 10,000 records and 12 columns related to orders, products, sales, quantity, discount, and profit.

## Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code

## Data Processing

The following operations were performed:

1. Read the CSV dataset using Pandas.
2. Analyzed the dataset structure and statistical summary.
3. Identified missing values.
4. Handled missing values using mean imputation.
5. Converted the Order Date column to datetime format.
6. Added Year, Month, and Month Name columns.
7. Generated meaningful business insights.
8. Created visualizations using Matplotlib.

## Missing Value Handling

Missing values were identified in the following columns:

- Sales
- Quantity
- Profit

Mean imputation was used to replace the missing numerical values.

After imputation, there were no remaining null values in the dataset.

## Key Insights

- **Total Sales:** 744,856.28
- **Total Profit:** 18,676.23
- **Total Quantity Sold:** 54,862 units
- **Highest Sales Category:** Office Supplies
- **Highest Sales Region:** Central
- **Highest Sales Year:** 2017
- **Highest Profit Category:** Furniture
- **Top State by Sales:** Michigan
- **Top Sub-Category by Sales:** Bookcases

## Visualizations

The project includes the following visualizations:

1. Sales by Category
2. Sales by Region
3. Year-wise Sales Trend
4. Top 10 States by Sales
5. Profit by Category

All generated charts are available in the `charts` folder.

## Project Structure

```text
4SF25CI173_3C/
│
├── superstore_sales.csv
├── sales_analysis.py
├── README.md
│
└── charts/
    ├── sales_by_category.png
    ├── sales_by_region.png
    ├── yearly_sales.png
    ├── top_10_states.png
    └── profit_by_category.png
```

## Conclusion

The project demonstrates the use of Python, Pandas, and Matplotlib for data preprocessing, missing value handling, data transformation, business insight generation, and visualization.
