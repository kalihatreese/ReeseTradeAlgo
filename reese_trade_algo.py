import numpy as np
import pandas as pd
import requests
import ta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

class ReeseAlgoTrade:
    def __init__(self):
        self.historical_data = None
        self.model = None

    def fetch_historical_data(self):
        # Fetch historical market data using Alpha Vantage API
        api_key = "b3434fff0a4c488887873bae494f7448"  # Replace with your Alpha Vantage API key
        symbol = "AAPL"  # Example symbol
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        self.historical_data = data

    def calculate_technical_indicators(self):
        # Calculate technical indicators using TA-Lib
        df = pd.DataFrame(self.historical_data['Time Series (Daily)']).T
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        df['macd'] = ta.trend.macd(df['4. close'])
        df['rsi'] = ta.momentum.rsi(df['4. close'])
        df['stoch'] = ta.momentum.stoch(df['2. high'], df['3. low'], df['4. close'])
        df['bb_bbm'], df['bb_bbh'], df['bb_bbl'] = ta.volatility.bollinger_hband(df['4. close']), ta.volatility.bollinger_hband_indicator(df['4. close']), ta.volatility.bollinger_lband(df['4. close'])
        self.historical_data = df

    def train_machine_learning_model(self):
        # Train machine learning model (HistGradientBoostingClassifier)
        X = self.historical_data[['macd', 'rsi', 'stoch', 'bb_bbm', 'bb_bbh', 'bb_bbl']]
        y = np.where(self.historical_data['4. close'].shift(-1) > self.historical_data['4. close'], 1, -1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Imputation - Replace missing values with the mean
        imputer = SimpleImputer(strategy='mean')
        X_train_imputed = imputer.fit_transform(X_train)
        X_test_imputed = imputer.transform(X_test)
        
        # Use HistGradientBoostingClassifier
        model = HistGradientBoostingClassifier()
        model.fit(X_train_imputed, y_train)
        self.model = model

        # Evaluate the model
        y_pred = model.predict(X_test_imputed)
        accuracy = accuracy_score(y_test, y_pred)
        print("Model Accuracy:", accuracy)

# Instantiate ReeseAlgoTrade
reese_algo_trade = ReeseAlgoTrade()

# Fetch historical market data
reese_algo_trade.fetch_historical_data()

# Calculate technical indicators
reese_algo_trade.calculate_technical_indicators()

# Train machine learning model
reese_algo_trade.train_machine_learning_model()
