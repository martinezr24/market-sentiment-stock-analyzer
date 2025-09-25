import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def compute_sentiment(news_df):
    # initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    print (sia.polarity_scores("OpenAI Adds Search Engine to ChatGPT, Challenging Google"))

    # making sure that all the headlines are strings and applying the sentiment analysis to them
    news_df['Headline'] = news_df['Headline'].astype(str)
    news_df['compound'] = news_df['Headline'].apply(lambda t: sia.polarity_scores(t)['compound'])

    # get the average of all headlines that day and return the dataframe
    daily_sent = news_df.groupby('Date')['compound'].mean().reset_index()
    daily_sent = daily_sent.rename(columns={'compound':'Sentiment'})
    daily_sent['Date'] = pd.to_datetime(daily_sent['Date'])
    return daily_sent