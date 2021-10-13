def multiply_list(list):
    product = 1

    for x in list:

        if type(x)==int or type(x)==float:
            product = product * x
        else:
            return False

    return product


Input = [1, 2, 3, 7]
print(multiply_list(Input))

Input = [3, 2, 4, 89]
print(multiply_list(Input))
