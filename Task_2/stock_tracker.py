stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

total = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter Stock Symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        investment = stock_prices[stock] * quantity
        total += investment
        print(f"{stock} Investment = ${investment}")
    else:
        print("Stock not available.")

print("\nTotal Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total}")

print("Portfolio saved successfully.")
