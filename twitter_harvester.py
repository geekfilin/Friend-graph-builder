import tweepy
import time
from .utils import rate_limit_handler

class TwitterHarvester:
    def __init__(self, api_config):
        self.auth = tweepy.OAuth1UserHandler(
            api_config['consumer_key'],
            api_config['consumer_secret'],
            api_config['access_token'],
            api_config['access_token_secret']
        )
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
    
    @rate_limit_handler
    def get_user_connections(self, username):
        user = self.api.get_user(screen_name=username)
        connections = {
            "user_id": user.id,
            "username": user.screen_name,
            "followers": [],
            "friends": []
        }
        
        for follower in tweepy.Cursor(self.api.get_followers, screen_name=username).items():
            connections['followers'].append({
                "id": follower.id,
                "username": follower.screen_name
            })
        
        for friend in tweepy.Cursor(self.api.get_friends, screen_name=username).items():
            connections['friends'].append({
                "id": friend.id,
                "username": friend.screen_name
            })
        
        return connections