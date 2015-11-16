import tweepy
import json
from tweepy import Stream
from sentiment import TwitterSentiment
from tweepy.streaming import StreamListener
from credentials import *

twitter = TwitterSentiment()
sentiments = []
topic = 'commodities'

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(token, token_secret)

class listener(StreamListener):

	def __init__(self, api=None):
		super(listener, self).__init__()
		self.tweets = 0

	def on_data(self, data):
		all_data = json.loads(data)
		tweet = all_data['text']

		self.tweets += 1
		if self.tweets < 1000:
			print(tweet)
			print('Current number of tweets: ' + str(self.tweets))
			sentiments.append(tweet)
			return True
		else:
			return False

	def on_error(self, status):
		print(status)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=[topic])

print('Sentiment for ' + topic + ': ' + twitter.get_sentiment(sentiments))
