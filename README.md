# 📈 Market Sentiment Stock Analyzer

This project analyzes the relationship between news sentiment and stock returns. It fetches stock price data and recent news headlines, computes sentiment scores using VADER (NLTK), and visualizes correlations in a Streamlit dashboard.

## 🚀 Features

- Fetch historical stock data ([Yahoo Finance](https://pypi.org/project/yfinance/))
- Fetch recent news headlines ([Finnhub API](https://finnhub.io/))
- Compute sentiment scores with VADER ([NLTK](https://www.nltk.org/))
- Plot correlation between sentiment and daily stock returns
- Test custom headlines for sentiment

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/market-sentiment-stock-analyzer.git
cd market-sentiment-stock-analyzer
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windowss
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Setup API Key

1. Sign up at [Finnhub API](https://finnhub.io/) and get a free API key.  
2. Update the `.env` file in the project root to add your API key:

```text
FINNHUB_API_KEY="YOUR_API_KEY_HERE"
```

## ▶️ Running the App

Run the program:

```bash
streamlit run analysis.py
```

## 📊 Example Output

- Scatter plot showing correlation between sentiment and stock returns.  
- Custom headline sentiment analysis displaying positive, neutral, negative, and compound scores.

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/) for the interactive dashboard  
- [NLTK](https://www.nltk.org/) for sentiment analysis  
- [Yahoo Finance](https://pypi.org/project/yfinance/) for stock data  
- [Finnhub API](https://finnhub.io/) for news headlines