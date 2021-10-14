from _future_ import division
def calculator(number1, number2, operator):
	result = 0
	if type(number1) == int or float and type(number2) == int or float and operator ('+','-','','/','//','**'):
		try
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
	except ZeroDivisionError:
			print("Can not devide by zero")
			return False

	return result
	else:
		print('Invalid')
		return False

def input_output():

	prompt = eval('input("Enter equation: ")')
	text = prompt.split(' ')
	if len(text) == 3:
		n1 = text[0]
		n2 = text[2]
		operator = text[1]
	else:
		print('invalid')
		exit()
	return calculator(n1,n2,operator)
