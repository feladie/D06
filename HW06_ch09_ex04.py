#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: Aloha coffee
#       2: Cool elf
#       3: Holla fella
##############################################################################
# Imports

# Body
def uses_only(word, letters):
	"""Returns True if the word contains only letters in the list.
	"""
	for alph in word:
		if alph.lower() not in letters:
			return False
	else:
		return True

def uses_only_words():
	"""Prints the words in words.txt that only contain letters in 'acefhlo'
	"""
    with open("words.txt", "r") as f:
        for line in f:  # for each line
            words = line.split()    # split the line into each word	
            for word in words:
            	if uses_only(word, 'acefhlo') == True:
            		print(word)

##############################################################################
def main():
	# print(uses_only('Hoe', 'acefhlo'))
	uses_only_words()

if __name__ == '__main__':
    main()
