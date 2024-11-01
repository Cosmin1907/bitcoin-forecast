import streamlit as st
import pandas as pd
import numpy as np
import requests
from src.data_management import load_pkl_file

# Function to fetch Bitcoin historical data from Binance
def load_bitcoin_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": "1d",
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if isinstance(data, dict) and 'code' in data:  # Check for error in response
        st.error(f"API Error: {data['msg']}")
        return None
    
    # Extract relevant columns and convert to DataFrame
    prices = pd.DataFrame(data, columns=["open_time", "open", "high", "low", "close", "volume", "close_time", 
                                         "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume", 
                                         "taker_buy_quote_asset_volume", "ignore"])
    
    # Convert data types
    prices['open'] = prices['open'].astype(float)
    prices['high'] = prices['high'].astype(float)
    prices['low'] = prices['low'].astype(float)
    prices['close'] = prices['close'].astype(float)
    prices['volume'] = prices['volume'].astype(float)
    
    # Rename the 'volume' column to 'Volume BTC'
    prices.rename(columns={'volume': 'Volume BTC'}, inplace=True)
    
    # Transform the time columns to datetime and set as index
    prices['open_time'] = pd.to_datetime(prices['open_time'], unit='ms')
    prices.set_index('open_time', inplace=True)
    
    return prices[['open', 'high', 'low', 'close', 'Volume BTC']]

# Function to create new features
def new_features(df):
    df['price mean'] = df[['open', 'high', 'low', 'close']].mean(axis=1)
    df['upper shadow'] = df['high'] - np.maximum(df['open'], df['close'])
    df['lower shadow'] = np.minimum(df['open'], df['close']) - df['low']
    df['spread'] = df['high'] - df['low']
    df['trade'] = df['close'] - df['open']
    df['10 period SMA'] = df['close'].rolling(10).mean().fillna(0)
    df['50 period SMA'] = df['close'].rolling(50).mean().fillna(0)
    df['100 period SMA'] = df['close'].rolling(100).mean().fillna(0)

    # Calculate MACD
    df['12EMA'] = df['close'].ewm(span=12, adjust=False).mean()
    df['26EMA'] = df['close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = df['12EMA'] - df['26EMA']

    # Calculate Volume USD from Volume BTC and current close price
    df['Volume USD'] = df['Volume BTC'] * df['close'] 

    # Calculate buy/sell signals
    df['buy/sell'] = df['close'].diff(periods=1)
    df = df.copy().loc[df['buy/sell'].notna()]  
    df['buy/sell'] = df['buy/sell'].apply(lambda x: 0 if x <= 0 else 1)  

    return df


# Load models for prediction
def load_models():
    regression_model = load_pkl_file("outputs/ml_pipeline/predict_close/v1/best_regressor_pipeline.pkl")
    classification_model = load_pkl_file("outputs/ml_pipeline/predict_buy_sell/v1/clf_pipeline_model.pkl")
    return regression_model, classification_model

# Make predictions using the models
def predict_price(model, input_data):
    return model.predict(input_data)

def predict_signal(model, input_data):
    return model.predict(input_data)

# Main function to encapsulate the forecast page logic
def page_forecast_body():
    st.header("Bitcoin Price Prediction and Buy/Sell Signal")
    
    # Load Bitcoin data
    bitcoin_data = load_bitcoin_data()
    if bitcoin_data is None:
        return  

    # Display the loaded Bitcoin data
    st.write("Historical Bitcoin Data:")
    st.dataframe(bitcoin_data)

    # Transform data to add new features
    bitcoin_data_transformed = new_features(bitcoin_data)

    # Display the transformed DataFrame
    st.write("Transformed Bitcoin Data with Features:")
    st.dataframe(bitcoin_data_transformed)
    
    # Get the most recent closing price 
    current_price = bitcoin_data['close'].iloc[-1]
    st.write(f"Current Bitcoin Price: ${current_price:,.2f}")

    # Prepare DataFrames for live prediction
    # Drop 'buy/sell' for regression, as it is the target for classification
    X_live_regression = bitcoin_data_transformed.drop(columns=['close'], errors='ignore')

    # Drop 'close' for classification, as it is the target for regression
    X_live_classification = bitcoin_data_transformed[['trade']]

    # Load models
    regression_model, classification_model = load_models()

    # Predict on live data
    if st.button("Run Predictions"):
        # Prediction with regression model
        price_prediction = predict_price(regression_model, X_live_regression)
        
        # Prediction with classification model
        signal_prediction = predict_signal(classification_model, X_live_classification)

        # Display results
        st.write(f"Predicted Bitcoin Price: ${price_prediction[0]:,.2f}")
        st.write(f"Predicted Signal: {'Buy' if signal_prediction[0] == 1 else 'Sell'}")





# If running as a standalone script, call main
if __name__ == "__main__":
    page_forecast_body()
