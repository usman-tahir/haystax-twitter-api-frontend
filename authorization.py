import json
from twitter import *

def generate_twitter_auth():
    config = json.load(open("config.json", "r"))
    twitter = Twitter(auth = OAuth(config["OAUTH_TOKEN"], config["OAUTH_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"]))
    return twitter