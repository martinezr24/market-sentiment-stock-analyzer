# 📈 Stock Sentiment vs Returns
This project analyzes the relationship between news sentiment and stock returns.
It fetches stock price data and recent news headlines, computes sentiment scores using VADER (NLTK), and visualizes correlations in a Streamlit dashboard.

n
🚀 Features
- Fetch historical stock data (via Yahoo Finance).
- Fetch recent news headlines (via Finnhub API).
- Compute sentiment scores with VADER.
- Plot correlation between sentiment and daily stock returns.
- Test custom headlines for sentiment.


🛠️ Installation
Clone the repo:
git clone https://github.com/YOUR_USERNAME/market-sentiment-stock-analyzer.git
cd market-sentiment-stock-analyzer

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt


🔑 Setup API Key
1. Sign up at **[Finnhub API](https://finnhub.io/)** and get a free API key.
2. Replace the API_KEY variable in the .env file with your API Key

▶️ Running the App
Type in terminal:
**streamlit run analysis.py**


📊 Example Output
Scatter plot showing correlation between sentiment and returns.
Custom headline sentiment analysis with positive, neutral, negative, and compound scores.


🙌 Acknowledgements
**[Streamlit](https://streamlit.io/)** for the dashboard
**[NLTK](https://www.nltk.org/)** for sentiment analysis
**[Yahoo Finance](https://pypi.org/project/yfinance/)** for stock data
**[Finnhub API](https://finnhub.io/)** for news headlines
