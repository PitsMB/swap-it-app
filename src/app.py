from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {
        "id": 1,
        "name": "Shoes1"
    },
    {
        "id": 2,
        "name": "Shoes2"
    },
    {
        "id": 3,
        "name": "Shoes3"
    }
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_items():
    item = request.get_json()
    items.append(item)
    return jsonify(items)

@app.route('/api/items/<item_id>', methods=['PUT'])
def edit_items(item_id):
    new_name = request.json['name']
    new_item = {
        "id": item_id,
        "name": new_name
    }

    
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
    
