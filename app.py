from flask import Flask, jsonify, request, abort, send_from_directory
from flask_cors import CORS
import uuid
import os

# serve files and API from project root
app = Flask(__name__, static_folder='.')
CORS(app)

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Expansive Watch A", "price": 85.00, "description": "Luxury analog watch with leather strap", "stock": 10, "image": "product 1.jpg"},
    {"id": 2, "name": "Expansive Watch B", "price": 75.00, "description": "Sporty chronograph watch", "stock": 8, "image": "product 2.jpg"},
    {"id": 3, "name": "Expansive Watch C", "price": 50.00, "description": "Minimalist watch with metal band", "stock": 15, "image": "product 3.jpg"},
    {"id": 4, "name": "Expansive Watch D", "price": 95.00, "description": "Automatic movement timepiece", "stock": 5, "image": "product 4.jpg"},
    {"id": 5, "name": "Expansive Watch E", "price": 76.00, "description": "Classic dress watch", "stock": 7, "image": "product 5.jpg"},
    {"id": 6, "name": "Expansive Watch F", "price": 85.00, "description": "Diver-style watch", "stock": 4, "image": "product 6.jpg"},
    {"id": 7, "name": "Expansive Watch G", "price": 94.00, "description": "Limited edition watch", "stock": 2, "image": "product 7.jpg"},
    {"id": 8, "name": "Expansive Watch H", "price": 70.00, "description": "Casual everyday watch", "stock": 20, "image": "product 8.jpg"},
    {"id": 9, "name": "Expansive Watch I", "price": 99.00, "description": "Premium sapphire crystal watch", "stock": 3, "image": "product 9.jpg"}
]

ORDERS = []

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/b.css')
def css():
    return app.send_static_file('b.css')


# Serve main.js and other frontend files from project root when they exist.


@app.route('/<path:filename>')
def serve_file(filename):
    # Ensure API routes are not overridden; only serve file if it exists in cwd
    if filename.startswith('api/'):
        abort(404)
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    abort(404)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    for p in PRODUCTS:
        if p['id'] == product_id:
            return jsonify(p)
    abort(404, description='Product not found')

@app.route('/api/checkout', methods=['POST'])
def checkout():
    data = request.get_json() or {}
    cart = data.get('cart')
    customer = data.get('customer')
    if not cart or not isinstance(cart, list):
        return jsonify({'error': 'Cart missing or invalid'}), 400

    # Simple validation and calculation
    total = 0.0
    for item in cart:
        pid = item.get('product_id')
        qty = int(item.get('quantity', 0))
        product = next((p for p in PRODUCTS if p['id'] == pid), None)
        if not product:
            return jsonify({'error': f'Product id {pid} not found'}), 400
        if qty > product['stock']:
            return jsonify({'error': f'Insufficient stock for product id {pid}'}), 400
        total += product['price'] * qty

    order_id = str(uuid.uuid4())
    ORDERS.append({'order_id': order_id, 'cart': cart, 'customer': customer, 'total': total})

    return jsonify({'success': True, 'order_id': order_id, 'total': total}), 201

@app.route('/api/orders', methods=['GET'])
def list_orders():
    return jsonify(ORDERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
