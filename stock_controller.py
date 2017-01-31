# Grabs stock information
# Python real-time stock: https://realtime-stock.readthedocs.io/en/latest/installation.html

from rtstock.stock import Stock
import unicodedata


def get_latest_price(name):
    # Returns the latest price the stock was traded at
    stock = Stock(name)
    return [str(stock.get_latest_price()[0]['LastTradePriceOnly'])]


if __name__ == '__main__':
    print get_latest_price("AAPL")
