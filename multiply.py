def multiply_list(list):

    product = 1

    for x in list:
        if type(x)==int or type(x)==float:
            product = product * x
        else:
	    print("invalid")
            return False
    return product

