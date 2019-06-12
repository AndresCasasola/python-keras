
import tweepy

consumer_key = 'BotArtic'
consumer_secret = 'ancado987'
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
