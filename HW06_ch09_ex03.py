#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
from string import ascii_lowercase

# Body


def avoids(word, forbidden):
    """ return True if word NOT forbidden"""
    for letter in forbidden:
        if letter in word:
            return False
    return True


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    forbidden = input("What are the forbidden letters? ")
    count = 0   # Number of words not forbidden by input
    with open("words.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if avoids(word, forbidden) == True:
                    count += 1
    print(str(count))


def forbidden_param(forbidden):
    """ return count of words NOT forbidden by param"""
    count = 0   # Number of words not forbidden by input
    with open("words.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if avoids(word, forbidden) == True:
                    count += 1
    return count

def total_words():
    """ Returns the total number of words within words.txt
    """
    total = 0
    with open("words.txt", "r") as f:
        for line in f:  # for each line
            words = line.split()    # split the line into each word
            total += len(words)   # add the number of words to the total
    return total

def find_five():
    """Prints the combination of five letters that excludes the least number of words.
        Prints the number of words excluded.
    """
    all_counts = []  # List of letters and the words that don't contain them
    combination = ''    # Combination of letters
    for alphabet in ascii_lowercase:
        count = forbidden_param(alphabet)   # Number of letters not excluded by forbidden paramater 
        letter_count = [count, alphabet]
        all_counts.append(letter_count)
    all_counts.sort()
    for number in range(1, 6):
        letter = all_counts[-number][1]
        combination += letter
    print(combination)
    excluded_words = total_words() - forbidden_param(combination)
    print(str(excluded_words))

# This function doesn't completely solve the problem because there might be the case 
# where the combination of words is in one word and one word only.


##############################################################################
def main():
    # print(avoids('Anna', 'Cho'))
    # print(avoids('Anna', 'N'))
    # forbidden_prompt()
    # print(forbidden_param('e'))
    # Your final submission should only call five_five
    # total_words()
    find_five()

if __name__ == '__main__':
    main()
