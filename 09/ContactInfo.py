class ContactInfo:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		
	def print_info(self):
		print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':
	sanghyun = ContactInfo('Park', 'ag@gamil.com')
	han = ContactInfo('han', 'han@gamil.com')
	
	sanghyun.print_info()
	han.print_info()
	#print('좋은날')
	