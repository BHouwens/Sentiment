from sentiment import TwitterSentiment

twitter = TwitterSentiment()
test_list = [
	'The comrades need bail money,lawyers  to represent them and people to be spreading the word #NationalShutDown'
]

print(twitter.get_sentiment(test_list))

