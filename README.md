# Stock Risk Calculator

A simple web application that calculates the risk score of a given stock based on user-defined parameters. The app uses the Yahoo Finance API to retrieve stock data and provides real-time risk scoring through a user-friendly interface.

## Features

- **Input Stock Ticker**: Enter the stock ticker symbol to analyze.
- **Adjustable Risk Holding Period**: Use a slider to specify how long you plan to hold the shares, with real-time updates to the risk score.
- **Real-time Risk Score Calculation**: Instantly see the risk score as you adjust the holding period.
- **Tooltips**: Hover over the question mark to learn more about how the risk score is calculated.
- **Minimalistic Design**: A clean and centered layout for a better user experience.
- **GitHub Repository Link**: View the project's source code at the bottom of the page.

## Technologies Used

- **Backend**: Python with Flask
- **API**: Yahoo Finance API via the `yfinance` library
- **Frontend**: HTML, CSS, JavaScript
- **Real-time Updates**: Fetching risk scores through AJAX calls

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sriveey/stock-calc.git
   cd stock-calc
   
2. Install the required Python packages:
   ```bash
   pip install Flask yfinance

3. Run the Flask app:
   ```bash
   python3 app.py
   
4. Open your web browser and go to http://127.0.0.1:8080 to access the application.
