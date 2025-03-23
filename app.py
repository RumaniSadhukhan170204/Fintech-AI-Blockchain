from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model (make sure fraud_model.pkl exists)
with open("fraud_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Ensure the JSON contains expected keys
        if not all(key in data for key in ["amount", "transaction_time", "location_change", "device_change"]):
            return jsonify({"error": "Missing required fields"}), 400

        # Convert input into DataFrame
        df = pd.DataFrame([data])

        # Convert transaction_time into total seconds
        df["transaction_time"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.hour * 3600 + \
                                 pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.minute * 60 + \
                                 pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.second

        # Make prediction
        prediction = model.predict(df)[0]
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"

        return jsonify({"fraud_flag": int(prediction), "result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)




