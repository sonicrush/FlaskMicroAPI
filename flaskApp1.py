from flask import Flask, jsonify, request
import json

app = Flask(__name__)
Hello = {"welcome_message": "Hello! Welcome to my API endpoint."}

@app.route("/")
def index():
    return ("<h1>Hello! Welcome to the root.<h1><br>"
            "<h2>The available API endpoints are <a href=/hello>/hello</a> and <a href=/data>/data</a></h2>"
            )

@app.route("/hello")
def hello():
    return jsonify(Hello)

@app.route("/data", methods=["GET","POST"])

def data() :
    try:
        json_data = open("data.json", "r")
        loaded_json=json.load(json_data)
        json_data.close()
        if request.method == "POST":
            return "POST request received!"
        else :
            return jsonify(loaded_json),200
    except Exception as e:
        return "Failed!"


if __name__ == "__main__":
    app.run()