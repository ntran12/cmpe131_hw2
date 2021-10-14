import time 

def calculate_time(function):
	def wrapper():
		start = time.time()
		function()
		end = time.time()
		total = end - start	
		print(f'Total time {total}')
	return wrapper

def hello():
	time.sleep(2)

hello_v2 = calculate_time(hello)

hello_v2()
