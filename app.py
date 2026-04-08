from flask import Flask, request, jsonify

app = Flask(__name__)

def run_agent(user_input):
    return f"Agent response to: {user_input}"

@app.route("/", methods=["GET"])
def home():
    return "Agent is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    result = run_agent(data.get("input", ""))
    return jsonify({"output": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)