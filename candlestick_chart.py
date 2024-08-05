import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from datetime import date, timedelta

# Set page configuration
st.set_page_config(page_title="Stock Candlestick Chart", layout="wide")

st.title("Stock Candlestick Chart")

# List of stock tickers
tickers = ["AAPL", "TSLA", "AMZN", "MSFT", "NVDA", "INTC"]

# Sidebar for selecting the stock and date range
selected_stock = st.sidebar.selectbox("Select a stock", tickers)

# Date range selection
end_date = date.today()
start_date = end_date - timedelta(days=365*10)  # Default to 10 years of data
start_date = st.sidebar.date_input("Start date", start_date)
end_date = st.sidebar.date_input("End date", end_date)

if start_date > end_date:
    st.sidebar.error("Error: End date must be after start date.")
    st.stop()

# Fetch stock data
@st.cache_data
def load_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end, threads=False)

stock_data = load_data(selected_stock, start_date, end_date)

if stock_data.empty:
    st.error(f"No data available for {selected_stock} in the selected date range.")
    st.stop()

# Create candlestick chart
candlestick = go.Figure(data=[go.Candlestick(
    x=stock_data.index,
    open=stock_data["Open"],
    high=stock_data["High"],
    low=stock_data["Low"],
    close=stock_data["Close"]
)])

# Customize chart layout
candlestick.update_xaxes(
    title_text="Date",
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1M", step="month", stepmode="backward"),
            dict(count=6, label="6M", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1Y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

candlestick.update_layout(
    title={
        'text': f"{selected_stock} Share Price ({start_date} to {end_date})",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    height=600,
)

candlestick.update_yaxes(title_text=f"{selected_stock} Close Price", tickprefix="$")

# Display the chart in Streamlit
st.plotly_chart(candlestick, use_container_width=True)

# Display additional stock information
st.subheader("Stock Information")
info = yf.Ticker(selected_stock).info
info_display = {
    "Company Name": info.get("longName", "N/A"),
    "Sector": info.get("sector", "N/A"),
    "Industry": info.get("industry", "N/A"),
    "Current Price": f"${info.get('currentPrice', 'N/A')}",
    "Market Cap": f"${info.get('marketCap', 'N/A'):,}",
    "52 Week High": f"${info.get('fiftyTwoWeekHigh', 'N/A')}",
    "52 Week Low": f"${info.get('fiftyTwoWeekLow', 'N/A')}",
}

st.table(pd.DataFrame([info_display]).T)
