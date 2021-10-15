def multiply_list(list):

"""

Multiply each element from list

Parameter
--------
number(string): hold input from user's prompt
list(list): list contain input from user
result (int): get result from multiplying whole list

if each element in list is valid, put them in list and multiply
else any element is invalid, immediately return False (invalid value)

"""
	result = 1

	for n in list:
		if type(n) == int or type(n) == float:
			result = result * n
		else:
			print("Invalid")
			return False
	return result

print(multiply_list([1,2,3,4,5]))


