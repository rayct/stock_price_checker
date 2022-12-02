import yfinance as yf
STK = input("Enter Share Name : ")
Share = yf.Ticker(STK).info
market_price = Share['regularMarketPrice']
print(market_price)

# rayturner.dev