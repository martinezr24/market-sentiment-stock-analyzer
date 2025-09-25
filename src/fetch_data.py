import finnhub
import yfinance as yf
import pandas as pd
from datetime import timedelta

API_KEY = ""
finnhub_client = finnhub.Client(api_key=API_KEY)


def fetch_stock_data(ticker, start, end):
    """
    fetch stock data for a ticker between start and end dates using yfinance.
    returns a DataFrame with normalized dates and daily returns.
    """
    df = yf.download(ticker, start=start, end=end)

    # flattens multi-indexed columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    # calculates the percent change between days
    df['return'] = df['Close'].pct_change()
    df = df.dropna().reset_index()
    
    # normalizes the dates in the Date column      
    df['Date'] = pd.to_datetime(df['Date']).dt.normalize()
    
    return df

def fetch_stock_headlines(symbol, start_date, end_date, chunk_days=30):
    """
    fetch headlines for a stock symbol between start_date and end_date,
    splitting the range into smaller chunks to maximize API data returned.
    """
    all_news = []
    current = start_date

    while current <= end_date:
        chunk_end = min(current + timedelta(days=chunk_days), end_date)

        news = finnhub_client.company_news(
            symbol,
            _from=current.strftime("%Y-%m-%d"),
            to=chunk_end.strftime("%Y-%m-%d"),
        )

        if news:
            all_news.extend(news)

        current = chunk_end + timedelta(days=1)
    
    if not all_news:
        return pd.DataFrame(columns=["Date", "Headline"])
    
    # convert to DataFrame and clean up
    news_df = pd.DataFrame(all_news)[["datetime", "headline"]].copy()
    news_df["Date"] = pd.to_datetime(news_df["datetime"], unit="s").dt.normalize()
    news_df.rename(columns={"headline": "Headline"}, inplace=True)

    return news_df[['Date', 'Headline']]