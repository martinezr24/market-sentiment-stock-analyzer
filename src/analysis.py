import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import pearsonr
from sentiment import compute_sentiment
from fetch_data import fetch_stock_data, fetch_stock_headlines
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.title("📈 Stock Sentiment vs Returns")

# sidebar inputs
st.sidebar.header("Analysis Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL, NFLX, TSLA):")
start = st.sidebar.date_input("From:")
end = st.sidebar.date_input("Until:")


if st.sidebar.button("Run Analysis"):
    """
    fetches stock and news data, computes sentiment,
    merges datasets, and displays correlation and plot.
    """

    with st.spinner("Fetching stock and news data..."):
        stock_df = fetch_stock_data(ticker, start, end)
        news_df = fetch_stock_headlines(ticker, start, end)

    # save results so they last
    st.session_state["stock_df"] = stock_df
    st.session_state["news_df"] = news_df

    # compute sentiment
    daily_sent = compute_sentiment(news_df)
    stock_df["Date"] = pd.to_datetime(stock_df["Date"]).dt.normalize()
    daily_sent["Date"] = pd.to_datetime(daily_sent["Date"]).dt.normalize()
    merged = stock_df.merge(daily_sent, on="Date", how="inner")
    st.session_state["merged"] = merged

    # -- display the analysis --
    if "stock_df" in st.session_state and "news_df" in st.session_state:
        stock_df = st.session_state["stock_df"]
        news_df = st.session_state["news_df"]
        merged = st.session_state["merged"]

        # show raw data
        st.subheader("Raw Stock Data")
        st.dataframe(stock_df.head())

        st.subheader("Raw News Headlines")
        st.dataframe(news_df.head())

        # merge stock and sentiment data
        st.subheader("Merged Data")
        st.dataframe(merged.head())

        # compute correlation and plot results
        if not merged.empty:
            r, p = pearsonr(merged["return"], merged["Sentiment"])
            st.write(f"**correlation**: {r:.4f} (p = {p:.4f})")

            # scatter plot with line of best fit
            fig, ax = plt.subplots(figsize=(8, 6))
            x, y = merged["Sentiment"], merged["return"]
            ax.scatter(x, y, alpha=0.7, label="data points")
            m, b = np.polyfit(x, y, 1)
            ax.plot(x, m * x + b, color="red", linewidth=2, label="best fit line")
            ax.set_xlabel("Daily Sentiment")
            ax.set_ylabel("Daily Return")
            ax.set_title(f"Sentiment vs Return: {ticker}")
            ax.axhline(0, color="black", linewidth=1, linestyle="--")
            ax.axvline(0, color="black", linewidth=1, linestyle="--")
            ax.grid(True, linestyle=":", alpha=0.5)
            ax.legend()
            st.pyplot(fig)
    else:
        st.warning("No merged data available. Try different dates or a different ticker.")

# -- gives the senitment score of a custom headline -- 
st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Test a Custom Headline")

custom_headline = st.sidebar.text_area("Enter a headline")
if custom_headline:
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(custom_headline)

    st.subheader("Sentiment Analysis of Custom Headline")
    st.write(f"**Headline:** {custom_headline}")
    # shows compound, pos, neu, neg scores
    st.json(scores) 