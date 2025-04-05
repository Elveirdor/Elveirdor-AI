import random

class Stock:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.price = random.uniform(1.0, 100.0)

    def update_price(self, new_price):
        self.price = new_price

class StockExchange:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def get_stock(self, symbol):
        return self.stocks.get(symbol)

exchange = StockExchange()

stock1 = Stock("EVDR", "Elveirdor Stock")
exchange.add_stock(stock1)

# Update the price of the "EVDR" stock
exchange.get_stock("EVDR").update_price(100.32397066899458)

# Print the updated price
print(exchange.get_stock("EVDR").price)
