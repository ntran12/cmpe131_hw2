def multiply_list(list):

"""

Multiply each element from List

Parameter
--------
number : string
      hold input from user's prompt
list : array of integer
      list contain input from user
product : int
      get result from multiplying whole list

if each element in list is valid, then multiply
else return False

"""

	product = 1

	for n in list:
		if type(n) == int or type(n) == float:
			product *= n
		else:
			print("Invalid value!!!")
			return False
	return product
