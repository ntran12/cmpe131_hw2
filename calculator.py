def calculator(number1, number2, operator):

	"""
	Do the calculate between two numbers

	Parameter
	--------
	n1 : float
	     hold the 1st operation
	n2 : float
	     hold the 2nd operation
	operator : string
	     hold the symbol of operator

	parse two number to float
        return false if the operator is not existence
	return result if operator is valid
	"""

	operation = ['+','-','*','/','//','**']

	if number1.isdigit() and number2.isdigit() and operator in operation:
		try:
			n1 = float(number1)
			n2 = float(number2)
			if operator == '+':
				result= n1 + n2
			elif operator == '-':
				result= n1 - n2
			elif operator == '*':
				result= n1 * n2
			elif operator == '/':
				result= n1 / n2
			elif operator == '//':
				result= n1 // n2
			elif operator == '**':
				result= n1 ** n2

	else:
		print('Invalid')
		return False

def parse_input():
	"""
	take the input from user and handle them

	parameter
	--------
	prompt : string
	       get input from user
	text : string
	       hold string from split
	n1 : string
	       contain 1st number
	n2 : string
	       contain 2nd number
	operator : string
	       contain 1

	get input from user
	split the input by a delimter that is space
	check user'input
	pass these values which just split to the calculator function with 3 parameters
	"""

	text = input('Enter equation: ').split()
	if len(text) == 3:
		n1,operator,n2 = text
		answer = calculator(n1,n2,operator)
		return answer
	else:
		return False
