def multiply_list(list):

    product = 1

    for x in list:
        if type(x) == int or type(x) == float:
            product *= x
        else:
	    print("invalid value!")
            return False
    return product

