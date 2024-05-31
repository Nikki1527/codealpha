import requests
import pandas as pd

API_KEY = 'your_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol]['shares'] += shares
        else:
            self.stocks[symbol] = {'shares': shares, 'price': 0, 'value': 0}

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks and self.stocks[symbol]['shares'] >= shares:
            self.stocks[symbol]['shares'] -= shares
            if self.stocks[symbol]['shares'] == 0:
                del self.stocks[symbol]
        else:
            print("Error: Not enough shares to remove or stock not in portfolio.")

    def update_stock_price(self, symbol, price):
        if symbol in self.stocks:
            self.stocks[symbol]['price'] = price
            self.stocks[symbol]['value'] = self.stocks[symbol]['shares'] * price

    def get_portfolio_value(self):
        return sum(stock['value'] for stock in self.stocks.values())

    def display_portfolio(self):
        portfolio_df = pd.DataFrame.from_dict(self.stocks, orient='index')
        print(portfolio_df)
        print(f"Total Portfolio Value: ${self.get_portfolio_value():.2f}")

def fetch_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Time Series (5min)' in data:
        last_refreshed = max(data['Time Series (5min)'].keys())
        price = float(data['Time Series (5min)'][last_refreshed]['4. close'])
        return price
    else:
        print(f"Error fetching data for {symbol}")
        return None

def main():
    if not API_KEY:
        print("Please provide your API key.")
        return

    portfolio = StockPortfolio()
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Prices")
        print("4. Display Portfolio")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            for symbol in portfolio.stocks.keys():
                price = fetch_stock_price(symbol)
                if price:
                    portfolio.update_stock_price(symbol, price)
        elif choice == '4':
            portfolio.display_portfolio()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
