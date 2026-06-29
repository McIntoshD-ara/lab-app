from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app) #automatically exposes /metrics endpoint

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Hello World!"})

@app.route("/health")
def health():
    return jsonify({"healthy": True})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
