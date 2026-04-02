import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.ppylot as plt
st.set_page_config(page_title="Stock Data Extraction App", layout="wide")
st.title ("Stock Data Extraction App")
st.write("Extract Stock Market Data From Yahoo Finance Using A Ticker Symbol")
st.sidebar.header("User Input")
ticker = st.sidebar.text_input("Enter Ticker", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))
#Download the data
if st.sidebar.button("Get Data"):

  # Create ticker object
  stock = yf.Ticker(ticker)

  #Download historical price data
  df = stock.history(start=start_date, end=end_date)

  # Check the data
  if df.empty:
    st.error("No data available for the selected ticker and date range.")

    else: 
      # show success message 
      st.success("Data successfully extracted for (ticker)")

      #display company information
      st.subheader("Company Information")
      info = stock.info

      company_name = info.get("longName", "N/A")
      sector = info.get("sector", "N/A")
      industry = info.get("industry", "N/A")
      market_cap = info.get("marketCap", "N/A")
      website = info.get("website", "N/A")

      st.write(f"Company Name: {company_name}")
      st.write(f"Sector: {sector}")
      st.write(f"Industry: {industry}")
      st.write(f"Market Cap: {market_cap}")
      st.write(f"Website: {website}")

      st.subheader("Historical Stock Data")
      st.dataframe(df)

      st.subheader("Closing Price Chart")
      fig, ax=plt.subplots()
      ax.plot(df.index, df["Close"])
      ax.set_xlabel("Date")
      ax.set_ylabel("Closing Price")
      ax.set_title(f"{company_name} Closing Price")
      st.pyplot(fig)

      CSV = df.to_csv().encode("utf-8")

      st.download_button(
          label="Download Data as CSV",
          data=CSV,
          file_name=f"{ticker}_stock_data.csv",
          mime="text/csv")
