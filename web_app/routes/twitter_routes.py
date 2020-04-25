# web_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, #render_template, request #, flash, redirect
from web_app.services.twitter_service import api as twitter_api

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
   print("Fetching...", screen_name)
   # TODO: fetch user info
   user = api.get_user(screen_name)
   # TODO: fetch user tweets
   statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
   # TODO: fetch embedding for each tweet
   
   # TODO: store user info in database
   # TODO: store tweets in database(w/ embeddings)
   
   return jsonify({"user": user._json, "num_tweets": len(statuses)})