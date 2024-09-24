import yfinance as yf
import numpy as np


# Make API Calls to Yahoo Finance to fetch stock price data
def get_stock_data(ticker):
    """
    Fetch stock data using yfinance.
    :param ticker: Stock ticker symbol as a string.
    :return: Stock data (historical prices) or None if the stock doesn't exist.
    """
    try:
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period="1y")  # Fetch 1 year of historical data
        
        if stock_data.empty:
            print(f"No data found for ticker: {ticker}")
            return None
        
        # Return the historical close prices
        return stock_data['Close']
    
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None


# Compute daily returns and calculate volatility
def calculate_volatility(stock_data):
    """
    Calculate the volatility of the stock based on historical data.
    :param stock_data: List or Series of historical stock prices.
    :return: Volatility score (standard deviation of returns).
    """
    try:
        # Calculate daily returns
        daily_returns = stock_data.pct_change().dropna()
        
        # Calculate the standard deviation (volatility)
        volatility = np.std(daily_returns) * np.sqrt(252)  # Annualized volatility
        
        return volatility
    
    except Exception as e:
        print(f"Error calculating volatility: {e}")
        return None


# Implement overall risk calculation
def calculate_risk(volatility, holding_period):
    """
    Calculate overall risk based on volatility and holding period.
    :param volatility: The calculated volatility score.
    :param holding_period: The holding period in months.
    :return: Risk score (higher is riskier).
    """
    try:
        # Basic risk formula: Volatility * sqrt(holding period)
        risk_score = volatility * np.sqrt(holding_period / 12)  # Adjusted for annual period
        
        return risk_score
    
    except Exception as e:
        print(f"Error calculating risk: {e}")
        return None
