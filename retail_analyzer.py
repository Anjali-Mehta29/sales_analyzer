
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:

    def __init__(self):
        self.df = None

    def load_data(self, file_path):

        if not file_path.lower().endswith(".csv"):
            print("Please select a CSV file.")
            return

        try:
            self.df = pd.read_csv(file_path)

            required_cols = ["Date", "Product", "Category", "Price",
                             "Quantity Sold", "Total Sales"]

            for col in required_cols:
                if col not in self.df.columns:
                    print("Required column missing:", col)
                    self.df = None
                    return

                self.df["Price"] = self.df["Price"].astype(float)
                self.df["Quantity Sold"] = self.df["Quantity Sold"].astype(float)
                self.df["Total Sales"] = self.df["Total Sales"].astype(float)
                self.df = pd.read_csv(file_path)


            self.df["Price"] = self.df["Price"].astype(float)
            self.df["Quantity Sold"] = self.df["Quantity Sold"].astype(float)
            self.df["Total Sales"] = self.df["Total Sales"].astype(float)

            self.df["Date"] = pd.to_datetime(self.df["Date"])

            self.df["Product"] = self.df["Product"].fillna("Unknown")
            self.df["Category"] = self.df["Category"].fillna("Unknown")

            self.df["Price"] = self.df["Price"].fillna(0)
            self.df["Quantity Sold"] = self.df["Quantity Sold"].fillna(0)

            self.df["Total Sales"] = self.df["Total Sales"].fillna(
                self.df["Price"] * self.df["Quantity Sold"])

            daily_sales = self.df.groupby("Date")["Total Sales"].sum()
            growth = daily_sales.pct_change().fillna(0) * 100
            self.df["Sales Growth"] = self.df["Date"].map(growth)

            print("\nDataset loaded successfully!")
            print("\nFirst Five Records:")
            print(self.df.head())

        except Exception as e:
            print("Error loading CSV file:", e)
            self.df = None

    def calculate_metrics(self):

        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        while True:

            print("\n---------- SALES METRICS ----------")

            print("1. Total Sales")
            print("2. Average Sales")
            print("3. Most Popular Product")
            print("4. Product-wise Sales")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            try:

                if choice == "1":

                    total_sales = np.sum(self.df["Total Sales"])
                    print("\nTotal Sales:", total_sales)

                elif choice == "2":

                    average_sales = np.mean(self.df["Total Sales"])
                    print("\nAverage Sales:", round(average_sales, 2))

                elif choice == "3":

                    product_sales = self.df.groupby("Product")["Quantity Sold"].sum()
                    popular_product = product_sales.idxmax()

                    print("\nMost Popular Product:", popular_product)

                elif choice == "4":

                    print("\nProduct-wise Sales:")
                    print(self.df.groupby("Product")["Total Sales"].sum())

                elif choice == "5":

                    break

                else:
                    print("\nInvalid choice! Please try again.")

            except Exception as e:
                print("\nUnable to calculate metrics:", e)

    def filter_data(self):

        if self.df is None:
            print("\nPlease load the dataset first!")
            return pd.DataFrame()

        print("\n---------- DATA FILTERING ----------")

        filtered_df = self.df.copy()

        while True:

            print("\n1. Filter by Category")
            print("2. Filter by Start Date")
            print("3. Filter by End Date")
            print("4. Display Filtered Data")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            try:

                if choice == "1":

                    print("\nAvailable Categories:")
                    print(self.df["Category"].unique())

                    category = input("\nEnter category: ")

                    filtered_df = filtered_df[
                        filtered_df["Category"].str.lower() == category.lower()]

                    print("\nCategory filter applied successfully!")

                elif choice == "2":

                    start_date = input("\nEnter start date (YYYY-MM-DD): ")

                    filtered_df = filtered_df[
                        filtered_df["Date"] >= pd.to_datetime(start_date)]

                    print("\nStart date filter applied successfully!")

                elif choice == "3":

                    end_date = input("\nEnter end date (YYYY-MM-DD): ")

                    filtered_df = filtered_df[
                        filtered_df["Date"] <= pd.to_datetime(end_date)]

                    print("\nEnd date filter applied successfully!")

                elif choice == "4":

                    if filtered_df.empty:
                        print("\nNo records found!")
                    else:
                        print("\nFiltered Dataset:")
                        print(filtered_df)

                        print("\nFiltered Total Sales:",
                              filtered_df["Total Sales"].sum())

                elif choice == "5":

                    return filtered_df

                else:
                    print("\nInvalid choice! Please try again.")

            except Exception as e:
                print("\nError while filtering data:", e)

    def display_summary(self):

        if self.df is None:
            print("\nPlease load the dataset first!")
            return

        while True:

            print("\n---------- SALES SUMMARY ----------")

            print("1. Total Sales by Category")
            print("2. Total Sales by Product")
            print("3. Daily Sales")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            try:

                if choice == "1":

                    print("\nTotal Sales by Category:")
                    print(self.df.groupby("Category")["Total Sales"].sum())

                elif choice == "2":

                    print("\nTotal Sales by Product:")
                    print(self.df.groupby("Product")["Total Sales"].sum())

                elif choice == "3":

                    print("\nDaily Sales:")
                    print(self.df.groupby("Date")["Total Sales"].sum())

                elif choice == "4":

                    break

                else:
                    print("\nInvalid choice! Please try again.")

            except Exception as e:
                print("\nUnable to display summary:", e)

    def visualize_data(self, data):

        if data.empty:
            print("\nNo data available for visualization.")
            return

        while True:

            print("\n---------- DATA VISUALIZATION ----------")

            print("1. Category-wise Sales Bar Graph")
            print("2. Sales Trend Line Graph")
            print("3. Sales Correlation Heatmap")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            try:

                if choice == "1":

                    category_sales = data.groupby(
                        "Category")["Total Sales"].sum().reset_index()

                    plt.figure(figsize=(9, 5))

                    sns.barplot(
                        data=category_sales,
                        x="Category",
                        y="Total Sales",
                        color="skyblue")

                    plt.title("Total Sales by Category")
                    plt.xlabel("Category")
                    plt.ylabel("Total Sales")
                    plt.xticks(rotation=30)
                    plt.tight_layout()
                    plt.show()

                elif choice == "2":

                    daily_sales = data.groupby(
                        "Date")["Total Sales"].sum().reset_index()

                    plt.figure(figsize=(10, 5))

                    sns.lineplot(
                        data=daily_sales,
                        x="Date",
                        y="Total Sales",
                        marker="o",
                        color="green")

                    plt.title("Sales Trend Over Time")
                    plt.xlabel("Date")
                    plt.ylabel("Total Sales")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

                elif choice == "3":

                    correlation = data[
                        ["Price", "Quantity Sold", "Total Sales"]].corr()

                    plt.figure(figsize=(7, 5))

                    sns.heatmap(
                        correlation,
                        annot=True,
                        cmap="coolwarm",
                        fmt=".2f")

                    plt.title("Sales Data Correlation Heatmap")
                    plt.tight_layout()
                    plt.show()

                elif choice == "4":
                    break

                else:
                    print("\nInvalid choice! Please try again.")

            except Exception as e:
                print("\nUnable to display graph:", e)


analyzer = RetailAnalyzer()

while True:

    print("\n========== RETAIL SALES DATA ANALYZER ==========")

    print("1. Load Dataset")
    print("2. Calculate Sales Metrics")
    print("3. Filter Sales Data")
    print("4. Display Sales Summary")
    print("5. Visualize Sales Data")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        file_path = input("\nEnter CSV file path: ")
        analyzer.load_data(file_path)

    elif choice == "2":

        analyzer.calculate_metrics()

    elif choice == "3":

        filtered_data = analyzer.filter_data()

    elif choice == "4":

        analyzer.display_summary()

    elif choice == "5":

        filtered_data = analyzer.filter_data()
        analyzer.visualize_data(filtered_data)

    elif choice == "6":

        print("\nThank you for using Retail Sales Data Analyzer!")
        break

    else:
        print("\nInvalid choice! Please try again.")
