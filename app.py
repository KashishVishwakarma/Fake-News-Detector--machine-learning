import os
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"

# Auto-train if files do not exist
if not os.path.exists(MODEL_FILE) or not os.path.exists(VECTORIZER_FILE):
    import train_model
    train_model.train()

# Load model and vectorizer into memory
with open(MODEL_FILE, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_FILE, "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Empty text provided"}), 400

    # Vectorize input and evaluate prediction
    transformed_text = vectorizer.transform([text])
    prediction = bool(model.predict(transformed_text)[0])

    return jsonify({
        "is_real": prediction,
        "label": "TRUE" if prediction else "FALSE",
        "description": "Verified / Factual reporting" if prediction else "Misinformation / Fabricated content"
    })

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
