import finnhub
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

api_key = ""
finnhub_client = finnhub.Client(api_key=api_key)

def fetch_stock_data(ticker, start, end):
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

def fetch_stock_headlines(symbol, start_date, end_date, chunk_days=30):
    """
    Fetch headlines for a stock symbol between start_date and end_date,
    splitting the range into smaller chunks to maximize results.
    """
    all_news = []
    current_start = start_date
    while current_start < end_date:
        current_end = min(current_start + timedelta(days=chunk_days), end_date)

        news = finnhub_client.company_news(
            symbol,
            _from=current_start.strftime('%Y-%m-%d'),
            to=current_end.strftime('%Y-%m-%d')
        )

        if news:
            all_news.extend(news)

        # move to the next chunk
        current_start = current_end + timedelta(days=1)
    
    # Convert to DataFrame
    news_df = pd.DataFrame(all_news)
    
    if news_df.empty:
        return pd.DataFrame(columns=['Date', 'Headline'])
    
    # Keep only relevant columns
    news_df = news_df[['datetime', 'headline']]
    
    # Convert timestamp to datetime
    news_df['Date'] = pd.to_datetime(news_df['datetime'], unit='s')
    
    # Normalize dates (remove time info)
    news_df['Date'] = news_df['Date'].dt.normalize()
    
    # Return only date and headline
    # print(news_df[['date', 'headline']])
    news_df['Headline'] = news_df['headline']
    return news_df[['Date', 'Headline']]


# def load_headlines(csv_path):
#     # read in the csv file and normalize the date column
#     news = pd.read_csv(csv_path, parse_dates=['date'])
#     news['date'] = pd.to_datetime(news['date']).dt.tz_localize(None).dt.normalize()

#     # only return a date and a headline column
#     news = news[['date', 'headline']]
#     return news[['date', 'headline']]