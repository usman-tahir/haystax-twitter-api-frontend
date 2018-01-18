from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from authorization import *

import random

app = Flask(__name__)
Bootstrap(app)
twitter_api = generate_twitter_auth()

@app.route("/")
def index():
    message = [
        "Search away!",
        "Enter search term here",
        "Looking for something?",
        "Example: Haystax Technology",
        "Example: moon landing",
        "What's on your mind?",
        "Sit back and search"
    ]
    return render_template("index.html", title = "Twitter API Frontend", message = random.choice(message))

@app.route("/search", methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        search = request.form["search"]
        result = twitter_api.request("search/tweets", {"q": "%s" % search, "count": 5, "exclude_replies": True})

        if result.status_code in [200, 304]:
            tweet_data = []
            for item in result.get_iterator():
                parsed_item = {
                    "datetime": item["created_at"],
                    "text": item["text"],
                    "english_word_count": 0
                }   
                tweet_data.append(parsed_item)
            if len(tweet_data) == 0:
                return render_template("blank.html")
            else:
                return render_template("search.html", search = search, tweets = tweet_data, count = len(tweet_data))
        else:
            return render_template("error.html", message = "Give us a moment while we determine what went wrong. Thank you for your patience!")

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")