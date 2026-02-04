import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description, get_expense_category
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "type", "expense_category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, txn_type, expense_category,  description):
        new_entry = {
            "date": date,
            "amount": amount,
            "type": txn_type,
            "expense_category": expense_category,
            "description": description,
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["type"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["type"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: Rs.{total_income:.2f}")
            print(f"Total Expense: Rs.{total_expense:.2f}")
            print(f"Net Savings: Rs.{(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    txn_type = get_category()  # must return "Income" or "Expense"
    description = get_description()
    if txn_type == "Expense":
        expense_category = get_expense_category()
    else:
        expense_category = ""
    
    CSV.add_entry(date, amount, txn_type, expense_category, description)

def plot_transactions(df):
    df = df.copy()  # avoid modifying caller's df
    df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
    df.set_index("date", inplace=True)

    # Ensure numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    income_df = (
        df[df["type"] == "Income"]
        .resample("D")["amount"]
        .sum()
    )

    expense_df = (
        df[df["type"] == "Expense"]
        .resample("D")["amount"]
        .sum()
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df, label="Income")
    plt.plot(expense_df.index, expense_df, label="Expense")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_expense_category_breakdown(df):
    df = df.copy()

    # Filter only expenses
    expense_df = df[df["type"] == "Expense"]

    if expense_df.empty:
        print("No expense data to plot.")
        return

    expense_summary = expense_df.groupby("expense_category")["amount"].sum()

    # Pie Chart
    plt.figure(figsize=(6, 6))
    expense_summary.plot.pie(
        autopct="%1.1f%%",
        startangle=90,
        shadow=True
    )
    plt.title("Expenses Breakdown by Category")
    plt.ylabel("")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8, 5))
    expense_summary.plot(kind="bar")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if not df.empty:
                if input("Do you want to see a time-series plot? (y/n) ").lower() == "y":
                    plot_transactions(df)

                if input("Do you want to see expense category charts? (y/n) ").lower() == "y":
                    plot_expense_category_breakdown(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()