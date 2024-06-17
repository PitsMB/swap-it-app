from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/items', methods=['GET'])
def get_items():
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
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
    

# @app.route('/api/items-details/', methods=['GET'])
# def find_items():
#     details = {'id': 1, 'name': 'shoes1'}
#     return details