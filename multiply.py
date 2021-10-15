def multiply_list(list):
	"""

	Multiply each element from list

	parameter
	----------
	number: string
		hold input from user's prompt
	list: array
		list conatin input from user
	result: int
		get result from whole list
	if each element in list is valid, then multiply
	else return false

	"""
    product = 1
    for x in list:
        if type(x) == int or type(x) == float:
            product *= x
        else:
	    print('invalid value!')
            return False
    return product

