class open2(object):
	def __init__(self, path):
		print('initialized')
		self.file = open(path)
		
	def __enter__(self):
		print('entered')
		return self.file
	
	def __exit__(self, ext, exv, trb):
		print("exited")
		self.file.close()
		return True
	
with open2("test.txt") as file: # 여기서 file은 그냥 객체 이름일 뿐이다.
	s = file.read()
	print(s)