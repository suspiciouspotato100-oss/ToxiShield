from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline

app = Flask(__name__)
CORS(app)

model_path = "textdetox/xlmr-large-toxicity-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = pipeline(text)[0]
    return jsonify({"label": result["label"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)