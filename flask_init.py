from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home</h1>"


@app.route("/test_json")
def test_json():

    data = {
        'field1': 'abc',
        'field2': 'def'
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
