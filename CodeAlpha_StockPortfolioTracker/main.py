
# CodeAlpha Internship
# Project: Stock Portfolio Tracker
# Currency: Indian Rupees (INR)

import csv
import os

stock_prices = {
    "RELIANCE": 1450,
    "TCS": 3200,
    "INFY": 1500,
    "HDFCBANK": 1750,
    "ICICIBANK": 1250
}

FILE_NAME = "portfolio.csv"

# Load saved portfolio
def load_portfolio():
    portfolio = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                stock = row["Stock"]
                quantity = int(row["Quantity"])

                if stock in stock_prices:
                    portfolio[stock] = (
                        portfolio.get(stock, 0) + quantity
                    )

    return portfolio


# Save portfolio
def save_portfolio(portfolio):
    with open(FILE_NAME, "w", newline="") as file:
        fields = ["Stock", "Price", "Quantity", "Investment"]

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]

            writer.writerow({
                "Stock": stock,
                "Price": price,
                "Quantity": quantity,
                "Investment": price * quantity
            })


# Add stock
def add_stock(portfolio):
    print("\nAvailable Indian Stocks:")

    for stock, price in stock_prices.items():
        print(f"{stock} - Rs.{price:,}")

    stock = input("\nEnter stock symbol: ").strip().upper()

    if stock not in stock_prices:
        print("Invalid stock symbol!")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        save_portfolio(portfolio)

        print(f"\n{stock} added successfully!")
        print(f"Total quantity: {portfolio[stock]}")
        print(f"Investment: Rs.{stock_prices[stock] * quantity:,}")

    except ValueError:
        print("Please enter a valid whole number.")


# View portfolio
def view_portfolio(portfolio):
    print("\n" + "=" * 55)
    print("                 YOUR PORTFOLIO")
    print("=" * 55)

    if not portfolio:
        print("Your portfolio is empty.")
        return

    total = 0

    print(f"{'STOCK':<15}{'QUANTITY':<12}{'PRICE':<12}{'VALUE':<15}")
    print("-" * 55)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        print(
            f"{stock:<15}{quantity:<12}"
            f"Rs.{price:<9,}Rs.{investment:,}"
        )

        total += investment

    print("-" * 55)
    print(f"TOTAL INVESTMENT: Rs.{total:,}")
    print("=" * 55)


# Main application
def main():
    portfolio = load_portfolio()

    while True:
        print("\n================================")
        print("     STOCK PORTFOLIO TRACKER")
        print("             INR")
        print("================================")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_stock(portfolio)

        elif choice == "2":
            view_portfolio(portfolio)

        elif choice == "3":
            save_portfolio(portfolio)
            print("\nPortfolio saved successfully!")
            print("Thank you for using Stock Portfolio Tracker.")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
