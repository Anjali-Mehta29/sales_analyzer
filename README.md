# Retail Sales Data Analyzer

## Subtitle of the Project

A simple Python project that loads, explores, filters, analyzes, and visualizes retail sales data using Pandas, NumPy, Matplotlib, and Seaborn.

## About the Project

This project is a beginner-friendly Python program that provides an interactive, menu-driven interface for analyzing retail sales data.

The program allows the user to select from the following options:

* Load retail sales data from a CSV file.
* Explore the dataset using `head()`, `columns`, and other Pandas operations.
* Convert the `Date` column from text to date format.
* Handle missing values in Product, Category, Price, Quantity Sold, and Total Sales columns.
* Calculate total sales and average sales.
* Identify the most popular product based on the total quantity sold.
* Display product-wise sales.
* Filter sales data by category.
* Filter sales data using a start date and end date.
* Display total sales by category and product.
* Display daily sales summaries.
* Calculate daily sales growth using `pct_change()`.
* Generate a bar chart to compare total sales by category.
* Generate a line chart to visualize sales trends over time.
* Generate a correlation heatmap to analyze relationships between numerical sales columns.
* Customize plots with titles, labels, and legends.
* Exit the program.

The program is organized using a `RetailAnalyzer` class. The class encapsulates the data loading, filtering, analysis, and visualization functionalities.

The project uses Pandas to load, clean, filter, and analyze retail sales data. NumPy is used for mathematical calculations. Matplotlib and Seaborn are used to create data visualizations.

The program handles exceptions during file loading, filtering, calculations, and visualization to manage invalid input and operation errors.

The program follows a structured workflow from dataset loading and cleaning to sales analysis, filtering, summary generation, and visualization.

## Features

* Displays a menu-driven interface for retail sales analysis.
* Loads retail sales data from a CSV file.
* Checks the CSV file extension before loading.
* Checks whether the required dataset columns are available.
* Explores datasets using Pandas functions.
* Converts the `Date` column into datetime format.
* Handles missing Product and Category values using `fillna()`.
* Handles missing Price and Quantity Sold values by replacing them with zero.
* Calculates missing Total Sales using Price multiplied by Quantity Sold.
* Calculates daily sales growth using `pct_change()`.
* Calculates total sales using NumPy.
* Calculates average sales using NumPy.
* Identifies the most popular product based on quantity sold.
* Displays product-wise sales.
* Filters sales records by category.
* Filters sales records using start and end dates.
* Displays filtered datasets and filtered total sales.
* Displays total sales by category.
* Displays total sales by product.
* Displays daily sales summaries.
* Generates bar charts to compare sales by category.
* Generates line charts to visualize sales trends over time.
* Generates correlation heatmaps to analyze relationships between Price, Quantity Sold, and Total Sales.
* Customizes charts using titles, labels, and axis rotation.
* Uses exception handling to manage file-related and operation errors.
* Uses class methods to organize different operations.
* Uses loops and conditional statements to manage menu selections.
* Allows the user to return to the main menu or exit the program.

## Concepts Used

* Variables and data types.
* User input and output.
* Functions and method calls.
* Classes and objects.
* Object-oriented programming.
* Pandas library.
* NumPy library.
* Matplotlib library.
* Seaborn library.
* DataFrames and Series.
* Reading CSV files using `pd.read_csv()`.
* Exploring datasets using `head()`, `columns`, and `copy()`.
* Date conversion using `pd.to_datetime()`.
* Handling missing values using `fillna()`.
* Grouping data using `groupby()`.
* Mathematical calculations using NumPy.
* Aggregation using `sum()` and `mean()`.
* Finding the most popular product using `idxmax()`.
* Calculating percentage changes using `pct_change()`.
* Data filtering using conditional expressions.
* Data visualization using Matplotlib and Seaborn.
* Creating bar charts using `barplot()`.
* Creating line charts using `lineplot()`.
* Creating correlation heatmaps using `heatmap()`.
* Calculating correlations using `corr()`.
* Plot customization using titles, labels, and axis rotation.
* Exception handling using `try` and `except`.
* Conditional statements using `if`, `elif`, and `else`.
* `while` loops.
* Menu-driven programming.
* Data analysis and visualization workflow.

## Built-in Functions and Methods Used

* `print()`
* `input()`
* `len()`
* `sum()`
* `round()`
* `lower()`
* `endswith()`
* `read_csv()`
* `head()`
* `copy()`
* `columns`
* `to_datetime()`
* `fillna()`
* `groupby()`
* `sum()`
* `mean()`
* `pct_change()`
* `map()`
* `unique()`
* `reset_index()`
* `idxmax()`
* `empty`
* `corr()`
* `figure()`
* `barplot()`
* `lineplot()`
* `heatmap()`
* `title()`
* `xlabel()`
* `ylabel()`
* `xticks()`
* `tight_layout()`
* `show()`
* `break`

## Technology Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* CSV
* Visual Studio Code (VS Code)
* Git
* GitHub

## About the Dataset

The retail sales dataset contains information about retail transactions, including product details, categories, dates, prices, quantities sold, and total sales.

| Column | Meaning |
|---|---|
| OrderID | Unique identification number of the order |
| Date | Date of the transaction |
| Product | Name of the product |
| Category | Category of the product |
| Quantity Sold | Number of units sold |
| Price | Price of the product |
| Total Sales | Total sales amount for the transaction |
| Region | Geographical region of the sale |
| PaymentMethod | Method used to complete the payment |

The dataset is used to analyze product performance, category-wise sales, daily sales trends, and relationships between numerical sales variables.

Missing values in the Product and Category columns are replaced with "Unknown". Missing numerical values are handled by replacing them with zero, and missing Total Sales values are calculated using Price multiplied by Quantity Sold.

## How to Run

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

### Step 2: Install Required Libraries

Open the terminal and run:

```bash
python -m pip install pandas numpy matplotlib seaborn
```

### Step 3: Open the Project

Open the project folder `retail_sales_analyzer` in Visual Studio Code.

### Step 4: Check the Dataset

Make sure the retail sales CSV file is available in the project directory or note its file path.

### Step 5: Run the Program

Open the terminal in the project directory and execute:

```bash
python retail_analyzer.py
```

### Step 6: Analyze Retail Sales Data

* Select the desired operation from the main menu.
* Load the retail sales dataset.
* Calculate sales metrics and identify popular products.
* Filter sales records by category and date.
* Display category-wise, product-wise, and daily sales summaries.
* Generate visualizations to understand sales patterns and trends.
* Return to the main menu or exit the program.

## Project Structure

```text
│
├── retail_analyzer.py
├── retail_sales.csv
└── README.md
```

## Learning Objectives

By completing this project, you can learn:

* How to load and analyze CSV datasets using Pandas.
* How to explore datasets using Pandas DataFrame methods.
* How to identify and handle missing values.
* How to convert text columns into date format.
* How to group data and calculate category-wise and product-wise sales.
* How to calculate total sales and average sales using NumPy.
* How to identify the most popular product.
* How to filter records using multiple conditions.
* How to calculate daily sales growth.
* How to create bar charts, line charts, and correlation heatmaps.
* How to customize visualizations using Matplotlib and Seaborn.
* How to use classes and methods to organize a Python program.
* How to handle invalid input using exception handling.
* How to use loops and conditional statements.
* How to create a menu-driven application.
* How to manage a Python project using VS Code, Git, and GitHub.

## Author

Anjali Mehta