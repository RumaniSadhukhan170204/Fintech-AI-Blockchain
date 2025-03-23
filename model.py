import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("transaction.csv")

# Convert 'transaction_time' to numeric features (hour, minute, second)
data['transaction_time'] = pd.to_datetime(data['transaction_time'], format='%H:%M:%S')
data['hour'] = data['transaction_time'].dt.hour
data['minute'] = data['transaction_time'].dt.minute
data['second'] = data['transaction_time'].dt.second

# Drop original time column
data.drop(columns=['transaction_time'], inplace=True)

# Features and labels
X = data[['amount', 'hour', 'minute', 'second', 'location_change', 'device_change']]
y = data['fraud_flag']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model as fraud_model.pkl
with open("fraud_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("✅ Model trained and saved successfully as fraud_model.pkl")


