from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path="")

@app.route("/", methods=["GET", "POST"])
def index():
    """Return the main page.  If the user has submitted any input, it will be rendered as output"""
    if request.method == "GET":
        # if this is the initial request for the page, just render the index
        return render_template("index.html")
    else:
        # if the user has submitted some data, retrieve it and send it as an argument
        data = request.form
        print(data)
        return render_template("index.html", user_output=data["user_input"])


