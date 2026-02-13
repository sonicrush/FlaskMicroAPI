from flask import Flask, jsonify
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
    return jsonify(Hello);

@app.route("/data")
def data() :
    try:
        jsonData = open("data.json", "r")
        return jsonify(json.load(jsonData)),200
    except Exception as e:
        return "Failed!"


if __name__ == "__main__":
    app.run()