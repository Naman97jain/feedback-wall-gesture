from flask import Flask , request, jsonify
from flask_cors import CORS
import feedback_functions
import json

app = Flask(__name__)
CORS(app)
records = []

@app.route("/feedback/update", methods=["POST"])
def update():
    data = request.get_json()
    feedback_functions.update_feedback(data)
    return get_alltime()
    

@app.route("/feedback/get/today", methods=["GET"])
def get_today():
    data = feedback_functions.get_today()
    return json.dumps(data, default=str), 200

@app.route("/feedback/get/alltime", methods=["GET"])
def get_alltime():
    data = feedback_functions.get_alltime()
    return json.dumps([x for x in data], default=str), 200

if __name__== '__main__':
    app.run(debug=True)