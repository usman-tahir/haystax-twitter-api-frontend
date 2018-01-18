from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from authorization import *

app = Flask(__name__)
Bootstrap(app)
twitter_api = generate_twitter_auth()

@app.route("/")
def hello_world():
    return render_template("index.html", title = "Twitter API Frontend")

@app.route("/search", methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        handle = request.form["handle"]
        return ("Handle searched: %s" % handle)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")