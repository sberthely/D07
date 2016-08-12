# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(numbers_list):
	cumulat_list = []
	for i in range(len(numbers_list)):
		if i == 0:
			cumulat_list.append(numbers_list[i])
		else:
			cumulat_list.append(numbers_list[i] + cumulat_list[i-1])
	return cumulat_list

def cumulative_sum2(numbers_list):
	cumulat_list = [0]
	running_sum = 0
	for item in numbers_list:
			numbers_list.append(item+numbers_list[-1])
	return cumulat_list[-1]
	
##############################################################################
def main():
	# numbers_list = [1, 5, 2, 7, 8]
	# cumulat_list = list()
	# cumulative_sum(numbers_list, cumulat_list)
	# print(cumulat_list)
	
	list_1 = [1, 2, 3]
	list_2 = [1, 3, 6]
	list_3 = [1]
	list_4 = [0, 0, 0, 1]
	print cumulative_sum(list_1)  # [1, 3, 6]
	print cumulative_sum(list_2)  # [1, 4, 10]
	print cumulative_sum(list_3)  # [1]
	print cumulative_sum(list_4)  # [0, 0, 0, 1]
	pass

if __name__ == '__main__':
    main()