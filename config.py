import twitter
from os import environ

def getApi():
	return twitter.Api(consumer_key=environ['CONSUMER_KEY'], 
					   consumer_secret=environ['CONSUMER_SECRET'], 
					   access_token_key=environ['ACCESS_KEY'], 
					   access_token_secret=environ['ACCESS_SECRET'])