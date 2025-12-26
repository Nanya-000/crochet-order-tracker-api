from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary storage for orders
orders = []

# Home route - API status
@app.route("/")
def home():
    return jsonify({"message": "Crochet Order Tracker API is running"})

# Get all orders
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

# Create a new order
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

# Run the app
if __name__ == "__main__":
    app.run(debug=True)