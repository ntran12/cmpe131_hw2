def calculator(number1, number2, operator):
	result = 0
	if number1.isdigit() == True and number2.isdigit() == True:
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
		print('Invalid value!!!')
		return False
	return result

def input_output():

	prompt = eval('input("Enter equation: ")')
	text = prompt.split(' ')
	n1 = text[0]
	n2 = text[2]
	operator = text[1]
	return calculator(n1,n2,operator)
