""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from collections import Counter

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	td = open(filename,'r')
	lines = td.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	curr_line2 = -1
	while lines[curr_line2].find("END OF THIS PROJECT GUTENBERG EBOOK") == -1:
		curr_line2 -= 1
	lines = lines[:curr_line2]
	#print lines

	stripped = []
	words = []

	for i in range(len(lines)):
		ls = lines[i].rstrip()
		lslower = ls.lower()
		output = lslower.translate(string.maketrans("",""), string.punctuation)
		stripped.append(output)

	for i in range(len(stripped)):
		words.extend(stripped[i].split())

	return words	

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
					"""
	topn = []

	wordcounts = Counter(word_list).most_common(n)

	for i in range(len(wordcounts)):
		word , count = wordcounts[i]
		topn.append(word)

	return topn

filename = 'the_defenders.txt'

DefendersList = get_word_list(filename)
top100 = get_top_n_words(DefendersList, 100)
print top100


