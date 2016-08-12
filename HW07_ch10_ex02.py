# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(user_list1):
	user_list_out = []
	for i in user_list1:
		if isinstance(i, list):
			user_list_out.append(capitalize_nested(i))
		else:
			user_list_out.append(str(i).capitalize())
			# print('word: ' + i)
			# user_list_out.append(i)
	return user_list_out
	# print(user_list2)


##############################################################################
def main():
	# user_list1 = ['apple', ['bear'], 'cat']
	# user_list_out = list()
	# capitalize_nested(user_list1, user_list_out)
	# print(user_list_out)
	
	list_1 = ['apple', ['bear'], 'cat', 'doggy', ['elbow', 'fin', 'garage']]
	list_2 = [[[['apple']], 'bear', 'cat', 'doggy', ['elbow','fin','garage','house','indigo']], 'jump']
	list_3 = []
	list_4 = ["doggy"]
	list_4 = [[[[[[["this"]]]]]]]
	print capitalize_nested(list_1)
	print capitalize_nested(list_2)
	print capitalize_nested(list_3)
	print capitalize_nested(list_4)

	pass

if __name__ == '__main__':
    main()