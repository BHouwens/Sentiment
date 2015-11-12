import nltk
import random
import pickle

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
from election import NLPElection


class Sentiment:
	'''
	General purpose sentiment analyser. It relies on pickled 
	training and testing sets as well as pretrained classifiers
	to work.
	'''
	def __init__(self, path):
		word_features5k_f = open(path, "rb")
		self.word_features = pickle.load(word_features5k_f)
		word_features5k_f.close()


	def train(self, nltk, mnb, bnb, lgr, svc):
		self.nltk_classifier_nb(nltk)
		self.multinomial_nb(mnb)
		self.bernoulli_nb(bnb)
		self.logistic_regress(lgr)
		self.linear_svc(svc)
		self.election()


	def find_features(self, document):
		words = word_tokenize(document)
		features = {}

		for word in self.word_features:
			features[word] = (word in words)

		return features


	def create_sets(self, path, boundary=60):
		'''
		This method is for creating training and testing
		sets for your classifiers. It actually has no use
		for this module, but serves as a reference
		'''
		featuresets_f = open(path, "rb")
		self.feature_sets = pickle.load(featuresets_f)
		featuresets_f.close()

		random.shuffle(self.feature_sets)
		length = len(self.feature_sets)
		limit = length * boundary / 100

		self.training_set = feature_sets[:limit]
		self.testing_set = feature_sets[limit:]


	def nltk_classifier_nb(self, path):
		open_file = open(path, "rb")
		self.classifier = pickle.load(open_file)
		open_file.close()


	def multinomial_nb(self, path):
		open_file = open(path, "rb")
		self.MNB_classifier = pickle.load(open_file)
		open_file.close()


	def bernoulli_nb(self, path):
		open_file = open(path, "rb")
		self.BernoulliNB_classifier = pickle.load(open_file)
		open_file.close()


	def logistic_regress(self, path):
		open_file = open(path, "rb")
		self.LogisticRegression_classifier = pickle.load(open_file)
		open_file.close()


	def linear_svc(self, path):
		open_file = open(path, "rb")
		self.LinearSVC = pickle.load(open_file)
		open_file.close()


	def election(self):
		self.election_classifier = NLPElection(
				self.classifier,
				self.MNB_classifier,
				self.BernoulliNB_classifier,
				self.LogisticRegression_classifier,
				self.LinearSVC
			)

	def analyse(self, data, lower_limit):
		self.sentiments = []

		for text in data:
			features = self.find_features(text)

			if self.election_classifier.unanimity(features) < lower_limit:
				self.sentiments.append(self.BernoulliNB_classifier.classify(features))
			else:
				self.sentiments.append(self.election_classifier.vote(features))


	def get_sentiment(self, data, lower_limit=0.4):
		self.analyse(data, lower_limit)
		total = len(self.sentiments)
		proportion = self.sentiments.count('pos') / total

		if proportion > 0.75:
			return 'very good'
		elif proportion > 0.5:
			return 'good'
		elif proportion > 0.25:
			return 'bad'
		else:
			return 'very bad'


class TwitterSentiment(Sentiment):
	def __init__(self):
		word_features5k_f = open("pickled/word_features5k.pickle", "rb")
		self.word_features = pickle.load(word_features5k_f)
		word_features5k_f.close()

		self.nltk_classifier_nb('pickled/originalnaivebayes5k.pickle')
		self.multinomial_nb('pickled/MNB_classifier5k.pickle')
		self.bernoulli_nb('pickled/BernoulliNB_classifier5k.pickle')
		self.logistic_regress('pickled/LogisticRegression_classifier5k.pickle')
		self.linear_svc('pickled/LinearSVC_classifier5k.pickle')
		self.election()



