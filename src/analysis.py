import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from fetch_data import fetch_stock_data, fetch_stock_headlines
from sentiment import compute_sentiment
import pandas as pd
import numpy as np
from datetime import datetime

#API_KEY = ""
ticker = "NFLX"
start = datetime(2025, 1, 1)
end = datetime(2025, 9, 24)

# load data
stock_df = fetch_stock_data(ticker, start, end)
news_df = fetch_stock_headlines(ticker, start, end)


print (stock_df)
print (news_df)

daily_sent = compute_sentiment(news_df)

# make the dates in each column the same type
stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.normalize()
daily_sent['Date'] = pd.to_datetime(daily_sent['Date']).dt.normalize()

print(stock_df)
print(daily_sent)

# merges stock and sentiment data and only keeps dates where there are both sentiments and stock data
merged = stock_df.merge(daily_sent, on='Date', how='inner')
print(merged)
# correlation
r, p = pearsonr(merged['return'], merged['Sentiment'])
print(f"Pearson correlation: {r:.4f}, p-value: {p:.4f}")

# plot

# add the plot points
plt.figure(figsize=(8, 6))
plt.scatter(merged['Sentiment'], merged['return'])


# line of best fit
x = merged['Sentiment']
y = merged['return']
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', linewidth=2, label='Best fit line')

# plot basics
plt.xlabel("Daily Sentiment")
plt.ylabel("Daily Return")
plt.title("Sentiment vs Return of " + ticker)
plt.axhline(0, color='black', linewidth=1, linestyle='--') 
plt.axvline(0, color='black', linewidth=1, linestyle='--')  
plt.grid(True, linestyle=':', alpha=0.5)
plt.show()