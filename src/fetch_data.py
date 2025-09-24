import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start, end):
    # get the stock data
    df = yf.download(ticker, start=start, end=end)

    # make sure the table is not multi-indexed
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    # calculates the percent change between days
    df['return'] = df['Close'].pct_change()
    df = df.dropna()
    
    # correctly indexes the entries and makes dates normalized
    df = df.reset_index()          
    df['Date'] = pd.to_datetime(df['Date']).dt.normalize()
    
    # returns a table of stock data over a period of time
    return df

def load_headlines(csv_path):
    # read in the csv file and normalize the date column
    news = pd.read_csv(csv_path, parse_dates=['date'])
    news['date'] = pd.to_datetime(news['date']).dt.tz_localize(None).dt.normalize()

    # only return a date and a headline column
    news = news[['date', 'headline']]
    return news[['date', 'headline']]