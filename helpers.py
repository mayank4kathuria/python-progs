# Implementing similaritiesusing python

from nltk.tokenize import sent_tokenize


def line(a,b):
	"""Get's lines , compares and find similar lines"""

	aline = list(a.split("\n"))
	bline = list(b.split("\n"))
	sim = []

	for x in aline:
		if x in bline:
			sim.append(x)

	sim = set(sim)

	return sim

def sentence(a,b):
	""" Split's stirng into sentenses , compares and return similar sentences"""

	a_sent = sent_tokenize(a)
	b_sent = sent_tokenize(b)
	sim= []

	for x in a_sent:
		if x in b_sent:
			sim.append(x)

	sim = set(sim)

	return sim

def substring(a,b,n):
	""" Extracts subString of length n from Strings"""

	a_sub = []
	b_sub = []
	sim = []

	for x in range(len(a) + 1 - n):
		a_sub.append(a[x:x+n])

	for x in range(len(b) + 1 - n):
		b_sub.append(b[x:x+n])

	for x in a_sub:
		if x in b_sub:
			sim.append(x)

	sim = set(sim)

	return sim