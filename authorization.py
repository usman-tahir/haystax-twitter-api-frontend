import json
from TwitterAPI import TwitterAPI

def generate_twitter_auth():
    config = json.load(open("config.json", "r"))
    api = TwitterAPI(config["CONSUMER_KEY"], config["CONSUMER_SECRET"], config["OAUTH_TOKEN"], config["OAUTH_SECRET"])
    return api