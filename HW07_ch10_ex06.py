# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(user_list):
	flag = True
	for i in range(len(user_list)-1):
		if user_list[i] > user_list[i+1]:
			flag = False
			break
	return flag
	# for element in user_list:
	# 	if element > user_list[]
	# numbers_list = numbers_list.sort()
	
##############################################################################
def main():
	# user_list = [89, 1, 23, 5, 2, 7, 2, 8, 6]
	# user_list = [1,2,3,4,5]
	# user_list = [1,2,3,4,3]
	# user_list = ['a', 'b', 'c']
	# print(is_sorted(user_list))

	list_1 = ['apple', 'bear', 'cat']
	list_2 = ['apple', 'bear', 'apples']
	list_3 = [1,2,3]
	list_4 = [1,45,3]
	list_5 = ['APPLE', 'BEAR', 'APPLES']
	list_6 = ['APPLE', 'BEAR', 'CAT']
	print is_sorted(list_1)  # True
	print is_sorted(list_2)  # False
	print is_sorted(list_3)  # True
	print is_sorted(list_4)  # False
	print is_sorted(list_5)  # False
	print is_sorted(list_6)  # True


	pass

if __name__ == '__main__':
    main()