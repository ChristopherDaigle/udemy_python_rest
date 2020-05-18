from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home</h1>"


@app.route("/test_json")
def test_json():
    """Function to test JSON return on web
    """
    name = "Chris"
    age = 34
    degrees = [
        {
            'first_degree': 'AAS Intelligence Operations',
            'second_degree': "BA Honors Economics with a Quantitative Emphasis, Math, Applied Math",
            'third_degree': "MS Quantitative Economics"
        }
    ]

    data = {
        'Name': name,
        'Age': age,
        'Degrees': degrees
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
