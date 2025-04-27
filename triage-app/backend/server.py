from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from flask_cors import CORS

# ------------------------------------------------------------------
# Model setup (done once, when the app starts)
# ------------------------------------------------------------------
MODEL_ID  = "VolodymyrPugachov/BioClinicalBERT-Triage"
SUBFOLDER = "checkpoint-6378"            # <- where the config & weights live

print("Loading BioClinicalBERT-Triage model …")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, subfolder=SUBFOLDER)
model     = AutoModelForSequenceClassification.from_pretrained(MODEL_ID,
                                                               subfolder=SUBFOLDER)
triage = pipeline("text-classification", model=model, tokenizer=tokenizer)
print("Model loaded!")

# ------------------------------------------------------------------
# Flask app
# ------------------------------------------------------------------
app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(silent=True)
    if not payload or "text" not in payload:
        return jsonify(error="POST JSON must contain a 'text' field"), 400

    result = triage(payload["text"])[0]      # returns e.g. {'label': 'urgent', 'score': 0.94}
    return jsonify(label=result["label"], score=result["score"])

if __name__ == "__main__":
    # threaded=False avoids duplicate model loads when debug=True reloads
    app.run(host="0.0.0.0", port=5001, debug=True, threaded=False)
