def tripler(function):
	def wrapper():
		function()
		function()
		function()
	return wrapper

@tripler
def say_hello():
	print("Hello")

say_hello()
