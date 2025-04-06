# Define a dictionary to store stocks and their prices
stocks = {
    "TSLA": 239.43,
    "GOOG": 134.81,
    "META": 514.77,
    "MSFT": 334.87,
    "JPM": 157.41,
    "ELVD": 50.00
}

# Define a dictionary to store user's shares
user_shares = {}

# Define a dictionary to store user's balance
user_balance = 1000000

def buy_shares(stock, quantity):
    global user_balance
    if stock in stocks:
        price = stocks[stock]
        total_cost = price * quantity
        if user_balance >= total_cost:
            user_balance -= total_cost
            if stock in user_shares:
                user_shares[stock] += quantity
            else:
                user_shares[stock] = quantity
            print(f"You bought {quantity} shares of {stock}.")
        else:
            print("You don't have enough balance to buy.")
    else:
        print("Invalid stock symbol.")

def sell_shares(stock, quantity):
    global user_balance
    if stock in user_shares:
        if user_shares[stock] >= quantity:
            price = stocks[stock]
            total_revenue = price * quantity
            user_balance += total_revenue
            user_shares[stock] -= quantity
            print(f"You sold {quantity} shares of {stock}.")
        else:
            print("You don't own enough shares to sell.")
    else:
        print("You don't own any shares of that stock.")

def display_portfolio():
    print("Your Portfolio:")
    for stock, quantity in user_shares.items():
        print(f"{stock}: {quantity} shares")

def display_balance():
    global user_balance
    print(f"Your balance: {user_balance}")

def calculate_stock_value(stock):
    if stock in stocks:
        price = stocks[stock]
        print(f"The value of {stock} is {price}.")
    else:
        print("Invalid stock symbol.")

def update_stock_prices():
    global stocks
    stocks["TSLA"] = 1700
    stocks["META"] = 1500
    stocks["GOOG"] = 5000
    stocks["AAPL"] = 1000
    stocks["ELVD"] = 950
    stocks["MSFT"] = 5000
    stocks["ЖПМ"] = 5000

def main():
    print("Welcome to the stock market simulation!")
    update_stock_prices()
    while True:
        print("Options:")
        print("1. Buy shares")
        print("2. Sell shares")
        print("3. Display portfolio")
        print("4. Display balance")
        print("5. Calculate stock value")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            stock = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            buy_shares(stock, quantity)
        elif choice == "2":
            stock = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            sell_shares(stock, quantity)
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            display_balance()
        elif choice == "5":
            stock = input("Enter the stock symbol: ")
            calculate_stock_value(stock)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Copyright (c) [2021] [Lauren Reed]
# ELVD (Elveirdor) Language
# Copyright Number: [TXu002252366]
# Copyright Information:
copyright_info = "Elveirdor (ELVD) Copyright Number: TXu002252366"

# Rest of your Python script...
