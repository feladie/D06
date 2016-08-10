def exercise3():
	"""Reads from roster.txt and prints the number of names containing an 'e'
		and lists the names containing an 'e'.
	"""

	count = 0 # number of names containing an e
	names_with_e = []
	with open("roster.txt", "r") as f:
		for line in f:	# for each line
			names_usernames = line.split()	# split the line into name and username
			first_name = names_usernames[0]	# name
			if 'e' in first_name.lower():	# if 'e' in name
				count += 1	# increase count
				names_with_e.append(first_name)	# add name to list
	print("Number of names containing the letter 'e': ", count)
	print(names_with_e)

def main():
	exercise3()

if __name__ == '__main__':
	main()