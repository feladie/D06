#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
	"""Returns True if the given word doesn't have the letter "e" in it.
	"""
	if 'e' not in word:
		return True

def print_no_e():
	"""Prints only the words in words.txt that have no "e" and prints the percentage
		of the words in the list that have no "e".
	"""
	count_no_e = 0 # number of words not containing an e
	total_words = 0 # total number of words
	words_without_e = []
	with open("words.txt", "r") as f:
		for line in f:	# for each line
			words = line.split()	# split the line into each word
			total_words += len(words)	# add the number of words to the total
			for word in words:
				if has_no_e(word) == True:
					count_no_e += 1
					print(word)
	percent = count_no_e / total_words * 100
	print("Percentage of words not containing an 'e': " + str(percent) + "%")


##############################################################################
def main():
	# print(has_no_e('Anna'))
	# print(has_no_e('Sleepy'))
	print_no_e()

if __name__ == '__main__':
	main()
