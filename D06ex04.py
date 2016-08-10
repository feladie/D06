def exercise4():
	"""Reads from roster.txt and prints the number of names containing 'e' 
		and lists those names into a new file, 'D06ex05.txt'.
	"""

	new_file = open('D06ex04.txt', 'w') # New file to add names and count to
	count = 0 # number of names containing an e
	names_with_e = []
	with open("roster.txt", "r") as f:
		for line in f:	# for each line
			names_usernames = line.split()	# split the line into name and username
			first_name = names_usernames[0]	# name
			if 'e' in first_name.lower():	# if 'e' in name
				count += 1	# increase count
				names_with_e.append(first_name)	# add name to list
	new_file.write("Number of names containing the letter 'e': " + str(count) + '\n') 
		# Writes count to new file
	new_file.write(str(names_with_e)) # Writes list of names into new file
	new_file.close()

def main():
	exercise4()

if __name__ == '__main__':
	main()