def multiply_list(list):
    '''
    	Multiply each elements in a list

	Parameter
	--------
	product: int/float: product of the list
	list(list): a list that contain number

	Returns the product of a list.
	If any item in the list is invalid, it returns False.

    '''
product = 1

    for x in list:

        if type(x)==int or type(x)==float:
            product = product * x
        else:
            return False

    return product

@testing
Input = [1, 2, 3, 7]
print(multiply_list(Input))

Input = [3, 2, 4, 89]
print(multiply_list(Input))
