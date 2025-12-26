from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Crochet Order Tracker API is running"
    })

if __name__ == "__main__":
    app.run(debug=True)

orders = []

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

@app.route("/orders", methods=["POST"])
def create_order():
    order = {
        "id": len(orders) + 1,
        "item": "Crochet Bag",
        "status": "pending"
    }
    orders.append(order)
    return jsonify(order), 201

from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route("/")
def home():
    return jsonify({"message": "Crochet Order Tracker API is running"})

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    order = {
        "id": len(orders) + 1,
        "item": data.get("item", "Unknown item"),
        "status": "pending"
    }
    orders.append(order)
    return jsonify(order), 201

if __name__ == "__main__":
    app.run(debug=True)