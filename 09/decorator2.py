class MyDecorator:
	def __init__(self, f):
		print("Initializing MyDecorator...")
		self.func = f
	
	def __call__(self):
		print("Begin : {0}".format(self.func.__name__))
		self.func()
		print("End : {0}".format(self.func.__name__))
	
@MyDecorator #이게 반드시 존재해야 print_hello()가 매개변수로 들어가게 됨
def print_hello(): 
	print("Hello.")
	
print_hello()
