from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
         {
        'id': 1,
        'Name': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
    }
]

@app.route("/app-data", methods=["POST"])
def add_task():
    if  not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide data"
        },400)