from flask import Flask, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

@app.route("/")
def home():
    return jsonify(message="Hello from CodeBuild demo")

@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify(result=add(a, b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
