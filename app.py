from flask import Flask, send_from_directory, render_template, request, redirect, url_for
from waitress import serve
from src.utils import text_processing
from src.models.predictor import get_prediction

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/make_prediction", methods=["POST"])
def make_prediction():
    """ Use the ML model to make a prediction using the form inputs. """

    # Get the data from the submitted form
    user_input = request.form['review_text'].strip()

    # Convert the data into just a list of values to be sent to the model
    feature_values = text_processing(user_input)

    # Send the values to the model to get a prediction
    prediction = get_prediction(feature_values)

    # Tell the browser to fetch the results page, passing along the prediction
    return redirect(url_for("show_results", prediction=prediction))

@app.route("/show_results")
def show_results():
    """ Display the results page with the provided prediction """
    
    # Extract the prediction from the URL params
    prediction = request.args.get("prediction")
    for result in prediction:
        label = prediction[2:-2]

    # Return the results pge
    return render_template("results.html", prediction=prediction, label=label)


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
