my_list = [1,2,3,4,5]

'''def print_element(arg,index):
	if index > 4:
		#raise Exception(IndexError)
		raise Exception()
	else :
		print(arg[index])

try:
	print('숫자를 입력하세요.')
	num = int(input())
	print_element(my_list,num)
except Exception as err:
	print("오류입니다.{0}".format(err))
	'''
def print_element(arg,index):
	try:
		print(arg[index])
	except IndexError as err:
		print("Invalid Number")
		
print_element(my_list,2)

print_element(my_list,7)
	
