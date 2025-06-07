from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Welcome to the Fraud Detection API! Use /predict to make predictions."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = [data['amount'], data['location'], data['timestamp']]
    prediction = model.predict([features])[0]
    return jsonify({"fraudulent": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
