from flask import Flask, jsonify

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
    

if __name__ == '__main__':
    app.run(debug=True)
    
