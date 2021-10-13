_list(lst):
    product = 1

    for x in lst:

        if type(x)==int or type(x)==float:
            product = product * x
        else:
            return False

    return product

###############################

# Testing
input = [1, 2, 3, 7]
print(multiply_list(input))

input = [3, 2, 4, 89]
print(multiply_list(input))
