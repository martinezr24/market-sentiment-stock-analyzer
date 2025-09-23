import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AAPL", start="2024-01-01", end="2024-12-01"):
    # get the stock data
    df = yf.download(ticker, start=start, end=end)

    # make sure the table is not multi-indexed
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    # calculates the percent change between days
    df['return'] = df['Close'].pct_change()
    df = df.dropna()
    
    #print (df)
    df = df.reset_index()          
    #print (df)
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df

def load_headlines(csv_path="data/apple_news_data.csv"):
    news = pd.read_csv(csv_path, parse_dates=['date'])
    return news[['date', 'headline']]
