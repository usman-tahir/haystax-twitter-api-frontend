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
        result = twitter_api.request("search/tweets", {"q": "%s" % handle, "count": 5})

        if result.status_code in [200, 304]:
            tweet_data = []
            for item in result.get_iterator():
                parsed_item = {
                    "datetime": item["created_at"],
                    "text": item["text"],
                    "english_word_count": 0
                }   
                tweet_data.append(parsed_item)
        else:
            return render_template("error.html", message = "Give us a moment while we determine what went wrong. Thank you for your patience!")

        return render_template("search.html", handle = handle, status = result.status_code, tweets = tweet_data)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")