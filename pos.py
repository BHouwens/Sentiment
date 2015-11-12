from nltk.corpus import wordnet

word = 'break'
syns = wordnet.synsets(word)

for entry in syns:
	if word not in entry.lemmas()[0].name():
		print entry.lemmas()[0].name() + ':'
		print entry.definition()
		print ' '


