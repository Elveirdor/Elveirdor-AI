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

import csv

# Load evdr data
evdr_data = []
with open('evdr_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        evdr_data.append(row)

# Load stock exchange data
stock_exchange_data = []
with open('stock_exchange_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stock_exchange_data.append(row)

# Define solution parameters
solution_params = {
    'thresholds': [
        {'min': 0, 'max': 1000, 'scale': 1700},
        {'min': 1500, 'max': 1700, 'scale': 0.95},
        {'min': 1700, 'max': 15000, 'scale': 1},
        {'min': 15000, 'max': 17000, 'scale': 0.5},
        {'min': 17000, 'max': 20000, 'scale': 0.1},
        {'min': 1000, 'max': 5000, 'scale': 0.2},
        {'min': 1500, 'max': 1700, 'scale': 0.1},
        {'min': 100, 'max': 500, 'scale': 0.95},
        {'min': 95, 'max': 100, 'scale': 1},
        {'min': 50, 'max': 100, 'scale': 0.5},
        {'min': 1, 'max': 5, 'scale': 1}
    ]
}

# Apply solution to data
def apply_solution(row):
    value = float(row['value'])
    for threshold in solution_params['thresholds']:
        if value >= threshold['min'] and value <= threshold['max']:
            return value * threshold['scale']
    return value

# Update stock exchange data
for row in stock_exchange_data:
    row['currency_decimal'] = apply_solution(row)

# Save updated stock exchange data to file
with open('stock_exchange_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=stock_exchange_data[0].keys())
    writer.writeheader()
    writer.writerows(stock_exchange_data)

