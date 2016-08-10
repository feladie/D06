# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list_param):
	total = 0
	for each_list in list_param:
		if isinstance(each_list, int):
			total += each_list
		else:
			total += nested_sum(each_list)	
	return total		



def main():
	# nested_sum([1, 2, [3]])
	# print(nested_sum([[1, [2]], 3, [[4, 5], 6]]))
	pass


if __name__ == '__main__':
	main()