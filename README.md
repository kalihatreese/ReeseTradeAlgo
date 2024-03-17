# ReeseTradeAlgo

ReeseTradeAlgo is a Python-based trading algorithm designed to analyze historical market data, calculate technical indicators, and predict price movements using machine learning techniques. This algorithm leverages data from the Alpha Vantage API for historical market data and TA-Lib for technical analysis.

## Features

- **Historical Data Retrieval:** Fetch historical market data from Alpha Vantage API.
- **Technical Indicator Calculation:** Calculate technical indicators such as MACD, RSI, stochastic oscillator, and Bollinger Bands.
- **Machine Learning Model Training:** Train a machine learning model (HistGradientBoostingClassifier) to predict price movements.
- **Model Evaluation:** Evaluate model accuracy using test data.

## Installation

To use ReeseTradeAlgo, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/ReeseTradeAlgo.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Replace the placeholder Alpha Vantage API key with your own key in the `fetch_historical_data` method of `ReeseAlgoTrade` class.

## Usage

To run ReeseTradeAlgo:

1. Navigate to the project directory.
2. Run the script:

    ```bash
    python reese_trade_algo.py
    ```

## Dependencies

- numpy
- pandas
- requests
- ta
- scikit-learn

## Contributing

We welcome contributions to improve ReeseTradeAlgo. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature/improvement
    ```

3. Make your changes and commit:

    ```bash
    git commit -am 'Add new feature'
    ```

4. Push to the branch:

    ```bash
    git push origin feature/improvement
    ```

5. Submit a pull request.

## License

This project is licensed under the [Insert License Name] License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [TA-Lib](https://github.com/mrjbq7/ta-lib): Technical Analysis Library
- [Alpha Vantage](https://www.alphavantage.co/): Financial Data API

## Contact

For any inquiries or support, please contact [Your Contact Information].
