from flask import Flask, request, jsonify

app = Flask(__name__)
logs = []

@app.route("/log", methods=["POST"])
def collect_log():
    data = request.json
    logs.append(data)
    return jsonify({"status": "received"})

@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)

if __name__ == "__main__":
    app.run(port=5000)
