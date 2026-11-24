
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:

    def __init__(self):
        self.df = None

    def load_data(self):
        try:
            print("\nLoad Dataset")
            file_path = input("Enter the path of the CSV file: ")
            self.df = pd.read_csv(file_path)

            self.df["Date"] = pd.to_datetime(self.df["Date"])

            # Calculate Sales Growth
            daily_sales = self.df.groupby("Date")["Total Sales"].sum()
            growth = daily_sales.pct_change().fillna(0) * 100
            self.df["Sales Growth"] = self.df["Date"].map(growth)

            print("\nDataset loaded successfully!")
            print("\nFirst Five Records:")
            print(self.df.head())

        except:
            print("Please enter a valid CSV file path! ")
            self.df = None

    def calculate_metrics(self):

        try:
            if self.df is None:
                print("\nPlease load the dataset first!")
                return

            print("\n---------- SALES METRICS ----------")
            print("1. Total Sales")
            print("2. Average Sales")
            print("3. Most Popular Product")
            print("4. Product-wise Sales")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                total_sales = np.sum(self.df["Total Sales"])
                print("\nTotal Sales:", total_sales)

            elif choice == 2:
                average_sales = np.mean(self.df["Total Sales"])
                print("\nAverage Sales:", round(average_sales, 2))

            elif choice == 3:
                product_sales = self.df.groupby("Product")["Quantity Sold"].sum()
                popular_product = product_sales.idxmax()
                print("\nMost Popular Product:", popular_product)

            elif choice == 4:
                print("\nProduct-wise Sales:")
                print(self.df.groupby("Product")["Total Sales"].sum())

            else:
                print("\nInvalid choice!")

        except:
            print("\nSomething went wrong! ")

    
    def filter_data(self):
        if self.df is None:
            print("\nPlease Load Dataset First!")
            return

        filtered_df = self.df.copy()

        while True:
            print("\n----- Filter Data -----")
            print("1. Filter By Category")
            print("2. Filter By Start Date")
            print("3. Filter By End Date")
            print("4. Display Filtered Data")
            print("5. Back To Main Menu")

            try:
                choice = input("\nEnter Your Choice: ")

                if choice == "1":
                    category = input("Enter Category: ")

                    filtered_df = filtered_df[
                        filtered_df["Category"].str.lower() == category.lower()
                    ]

                    print("\nCategory Filter Applied Successfully!")

                elif choice == "2":
                    start_date = input("Enter Start Date (YYYY-MM-DD): ")

                    filtered_df = filtered_df[
                        filtered_df["Date"] >= pd.to_datetime(start_date)
                    ]

                    print("\nStart Date Filter Applied Successfully!")

                elif choice == "3":
                    end_date = input("Enter End Date (YYYY-MM-DD): ")

                    filtered_df = filtered_df[
                        filtered_df["Date"] <= pd.to_datetime(end_date)
                    ]

                    print("\nEnd Date Filter Applied Successfully!")

                elif choice == "4":

                    if filtered_df.empty:
                        print("\nNo Records Found!")

                    else:
                        print("\nFiltered Data:")
                        print(filtered_df)

                        print("\nFiltered Total Sales:",
                            filtered_df["Total Sales"].sum())

                elif choice == "5":
                    break

                else:
                    print("\nInvalid Choice!")

            except:
                print("\nSomething went wrong!")

    def display_summary(self):

        try:
            if self.df is None:
                print("\nPlease load the dataset first!")
                return

            print("\n---------- SALES SUMMARY ----------")
            print("1. Total Sales by Category")
            print("2. Total Sales by Product")
            print("3. Daily Sales")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                print("\nTotal Sales by Category:")
                print(self.df.groupby("Category")["Total Sales"].sum())

            elif choice == 2:
                print("\nTotal Sales by Product:")
                print(self.df.groupby("Product")["Total Sales"].sum())

            elif choice == 3:
                print("\nDaily Sales:")
                print(self.df.groupby("Date")["Total Sales"].sum())

            else:
                print("\nInvalid choice!")

        except:
            print("\nSomething went wrong!")

    def visualize_data(self):
        try:
            if self.df is None:
                print("\nPlease load the dataset first!")
                return

            print("\n---------- DATA VISUALIZATION ----------")
            print("1. Category-wise Sales Bar Graph")
            print("2. Sales Trend Line Graph")
            print("3. Sales Correlation Heatmap")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:

                category_sales = self.df.groupby("Category")["Total Sales"].sum().reset_index()

                plt.figure(figsize=(9, 5))

                sns.barplot(
                    data=category_sales,
                    x="Category",
                    y="Total Sales",
                    color="skyblue")

                plt.title("Total Sales by Category")
                plt.xlabel("Category")
                plt.ylabel("Total Sales")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif choice == 2:

                daily_sales = self.df.groupby("Date")["Total Sales"].sum().reset_index()

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

            elif choice == 3:

                correlation = self.df[["Price", "Quantity Sold", "Total Sales"]].corr()

                plt.figure(figsize=(7, 5))
                sns.heatmap(
                    correlation,
                    annot=True,
                    cmap="coolwarm",
                    fmt=".2f")

                plt.title("Sales Data Correlation Heatmap")
                plt.tight_layout()
                plt.show()

            else:
                print("\nInvalid choice!")

        except:
            print("\nSomething went wrong")


    def main_menu(self):

        while True:
            print("\n========== RETAIL SALES DATA ANALYZER ==========")
            print("1. Load Dataset")
            print("2. Calculate Sales Metrics")
            print("3. Filter Sales Data")
            print("4. Display Sales Summary")
            print("5. Visualize Sales Data")
            print("6. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except:
                print("\nPlease enter a number!")
                continue

            if choice == 1:
                self.load_data()

            elif choice == 2:
                self.calculate_metrics()

            elif choice == 3:
                self.filter_data()

            elif choice == 4:
                self.display_summary()

            elif choice == 5:
                self.visualize_data()

            elif choice == 6:
                print("\nThank you for using Retail Sales Data Analyzer!")
                break

            else:
                print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    obj = RetailAnalyzer()
    obj.main_menu()
