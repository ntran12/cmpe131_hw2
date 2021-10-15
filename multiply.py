def multiply_list(list):

"""
	Multiply each elements from list

	Parameter
	---------
	number: string:
		hold input from user's prompt
	list: array:
		list contain input from user
	result: int
		get result from multiply whole list

	if each element in list í valid, put them in list and multiply
	else, return false



"""
    product = 1

    for x in list:

        if type(x)==int or type(x)==float:
            product = product * x
        else:
	    print("invalid")
            return False

    return product

print(multiply_list([1,2,3,4,5]))
