from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Sum API is running. Use /sum?a=1&b=2"

@app.route("/sum")
def sum_route():
    # Get query params a and b
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return jsonify({
            "error": "Please provide query params a and b, e.g. /sum?a=1&b=2"
        }), 400

    result = a + b
    return jsonify({
        "a": a,
        "b": b,
        "sum": result
    })

if __name__ == "__main__":
    # Local test
    app.run(host="0.0.0.0", port=8080)
