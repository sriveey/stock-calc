from flask import Flask, jsonify, request, send_from_directory
from backend import calculate_risk, calculate_volatility, get_stock_data
import os

app = Flask(__name__)

@app.route('/risk', methods=['GET'])
def get_risk():
    ticker = request.args.get('ticker')
    holding_period = int(request.args.get('holding_period', 12))

    stock_data = get_stock_data(ticker)
    if stock_data is None:
        return jsonify({"error": "No stock data available"}), 400
    
    volatility = calculate_volatility(stock_data)
    if volatility is None:
        return jsonify({"error": "Could not calculate volatility"}), 500
    
    risk_score = calculate_risk(volatility, holding_period)
    return jsonify({"ticker": ticker, "risk_score": risk_score})

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
