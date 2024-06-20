from flask import Flask, jsonify, request, redirect, Response

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

@app.route('/api/items')
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>')
def get_item_by_id(item_id):
    return_id_value = {}
    for id_to_find in items:
        if id_to_find['id'] == item_id:
            return_id_value = id_to_find
    return jsonify(return_id_value)

@app.route('/api/items/<string:item_name>')
def get_item_by_name(item_name):
    return_name_value = {}
    for name_to_find in items:
        if name_to_find['name'] == item_name:
            return_name_value = name_to_find
    return jsonify(return_name_value)

@app.route('/api/items', methods=['POST'])
def add_items():
    item = request.get_json()
    items.append(item)
    return jsonify(items)

@app.route('/api/items/<int:id_to_edit>', methods=['PUT'])
def edit_item_by_id(id_to_edit):
    print(type(id_to_edit))
    request_data = request.get_json()
    updated_item = {
        'id': id_to_edit,
        'name': request_data['name'] 
    }
    for item in items:
        if item['id'] == id_to_edit:
            item.update(updated_item)
    return jsonify(updated_item)

@app.route('/api/items/<int:id_to_delete>', methods=['DELETE'])
def delete_item(id_to_delete):
    for index, item in enumerate(items):
        if item['id'] == id_to_delete:
            del items[index]
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
    
