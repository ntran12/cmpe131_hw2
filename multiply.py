def multiply_list(list):

	product = 1

	for n in list:
		if type(n) == int or type(n) == float:
			product *= n
		else:
			print("Invalid value!!!")
			return False
	return product
