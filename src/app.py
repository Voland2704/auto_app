from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Dummy data as a substitute for a database
items = [
    {"id": 1, "name": "Item 1", "description": "Description 1"},
    {"id": 2, "name": "Item 2", "description": "Description 2"},
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/search', methods=['GET'])
def search_items():
    item_id = request.args.get('item_id', type=int)
    item = next((item for item in items if item['id'] == item_id), None)
    message = "Item not found" if item is None else None
    message = item
    return render_template('index.html', Item=item, message=message)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = {
        "id": len(items) + 1,
        "name": request.json['name'],
        "description": request.json['description'],
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item['name'] = request.json['name']
        item['description'] = request.json['description']
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
