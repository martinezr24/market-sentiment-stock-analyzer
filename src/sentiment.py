import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


nltk.download('vader_lexicon')

def compute_sentiment(news_df):
    # initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # making sure that all the headlines are strings and applying the sentiment analysis to all the headlines
    news_df['headline'] = news_df['headline'].astype(str)
    news_df['compound'] = news_df['headline'].apply(lambda t: sia.polarity_scores(t)['compound'])
    # get the average of all headlines that day and return the dataframe
    daily_sent = news_df.groupby('date')['compound'].mean().reset_index()
    daily_sent = daily_sent.rename(columns={'date': 'Date', 'compound':'sentiment'})
    daily_sent['Date'] = pd.to_datetime(daily_sent['Date'])
    return daily_sent