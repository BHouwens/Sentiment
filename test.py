from sentiment import TwitterSentiment

twitter = TwitterSentiment()
test_list = [
	'New ways to use old information 》Move Over, Humans: Next Evolution in #Science? @Ayasdi http://bit.ly/1LMnmAC  #BigData #machinelearning',
	'Get 50+ *free* #DataScience Books at http://bit.ly/1Or1j5Z   #abdsc #BigData #Analytics #MachineLearning ',
	'Dispel Pulp Fiction: Real Machine Intelligence Bleeding Edge: https://www.linkedin.com/pulse/real-machine-intelligence-bleeding-edge-david-ray?published=u … @homeAIinfo #machinelearning',
	'Musical Genres Classified Using Entropy  | MIT Tech http://bit.ly/1NtigtK  #DataScience #MachineLearning ',
	'New NVIDIA hyperscale accelerators boost #machinelearning workloads to enable new #AI apps. http://nvda.ly/UufTy',
	'An Amazing Tour of Machine Learning Algorithms @TeachTheMachine http://ow.ly/SYL6k  #machinelearning #bigdata ',
	'Blueberry picking robot could win $250,000 prize | http://goo.gl/fdm6vs  #Robotics #MachineLearning #AI #Challenge'
]

sentiments = []

for entry in test_list:
	sentiments.append(twitter.analyse(entry)[0])

pos_count = sentiments.count('pos')
neg_count = sentiments.count('neg')

if pos_count > neg_count:
	print('sentiment is positive')
else:
	print('sentiment is negative')