import random

def exercise_02():
	""" Prints 10 random integers between 0 and 100 into the text file 'D06ex02.txt'.
	"""
	f = open('D06ex02.txt', 'w')
	for number in range(0, 10):
		f.write(str(random.randrange(100)) + ' ')
	f.close()

def main():
	exercise_02()

if __name__ == '__main__':
	main()