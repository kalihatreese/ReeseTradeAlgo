import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier

# Load the historical stock data
historical_data = pd.read_csv('stock_data.csv')

# Drop any missing values
historical_data.dropna(inplace=True)

# Create features and target variables
features = historical_data[['macd', 'rsi', 'stoch', 'bb_bbm', 'bb_bbh', 'bb_bbl']]
target_classification = (historical_data['Close'].shift(-1) > historical_data['Close']).astype(int)
target_regression = historical_data['Close']

# Split the data into training and test sets
X_train, X_test, y_train_classification, y_test_classification = train_test_split(features, target_classification, test_size=0.2, random_state=42)
X_train, X_test, y_train_regression, y_test_regression = train_test_split(features, target_regression, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the classification model
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train_scaled, y_train_classification)

# Train the regression model
regressor = LinearRegression()
regressor.fit(X_train_scaled, y_train_regression)

# Evaluate the classification model on the test set
score_classification = classifier.score(X_test_scaled, y_test_classification)
print("Classification Score:", score_classification)

# Evaluate the regression model on the test set
score_regression = regressor.score(X_test_scaled, y_test_regression)
print("Regression Score:", score_regression)

# Make a classification prediction
new_data = pd.DataFrame({
    'macd': [0.1],
    'rsi': [50.0],
    'stoch': [80.0],
    'bb_bbm': [100.0],
    'bb_bbh': [110.0],
    'bb_bbl': [90.0]
})

new_data_scaled = scaler.transform(new_data)
prediction_classification = classifier.predict(new_data_scaled)

# Make a regression prediction
prediction_regression = regressor.predict(new_data_scaled)

# Print the predictions
print("Classification Prediction:", prediction_classification)
print("Regression Prediction:", prediction_regression)