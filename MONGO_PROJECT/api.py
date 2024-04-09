from bson import ObjectId
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_management"]
products_collection = db["products"]

@app.route("/products", methods=["GET"])
def get_products():
    # Implement logic to retrieve all products or filter based on query parameters
    # Example: /products?category=Electronics&min_price=100&max_price=500
    criteria = {}
    category = request.args.get("category")
    if category:
        criteria["category"] = category
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")
    if min_price and max_price:
        criteria["price"] = {"$gte": float(min_price), "$lte": float(max_price)}
    products = list(products_collection.find(criteria))
    return jsonify(products)

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    # Implement logic to retrieve a product by ID
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

# Implement other CRUD endpoints (POST, PUT, DELETE) similarly

if __name__ == "__main__":
    app.run(debug=True)
