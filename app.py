from flask import Flask, send_from_directory, render_template, request, abort
from waitress import serve
from models.wine_predictor import predict_wine

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/get_results", methods=["POST"])
def get_results():
    """ Predict the class of wine based on the inputs. """
    data = request.form
    print(data)

    expected_features = ("Alcohol", "Malic acid", "Ash", "Alcalinity of ash",
                         "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols",
                         "Proanthocyanins", "Color intensity", "Hue",
                         "OD280/OD315 of diluted wines", "Proline")

    if data and all(feature in data for feature in expected_features):
        # Convert the dict of fields into a list
        test_value = [float(data[feature]) for feature in expected_features]
        predicted_class = predict_wine(test_value)
        return render_template("results.html", predicted_class=predicted_class)
    else:
        return abort(400)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
