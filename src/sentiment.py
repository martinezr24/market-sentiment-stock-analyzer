import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def compute_sentiment(news_df):
    '''
    takes in a DataFrame of headlines and dates and applies a sentiment analysis to each entry.
    '''
    sia = SentimentIntensityAnalyzer()

    # makes sure each headline is a string and then applies the sentiment analysis to each one
    news_df['Headline'] = news_df['Headline'].astype(str)
    news_df['compound'] = news_df['Headline'].apply(lambda t: sia.polarity_scores(t)['compound'])

    # get the average of all headlines that day and return the dataframe
    daily_sent = news_df.groupby('Date')['compound'].mean().reset_index()
    daily_sent = daily_sent.rename(columns={'compound':'Sentiment'})
    daily_sent['Date'] = pd.to_datetime(daily_sent['Date'])
    return daily_sent