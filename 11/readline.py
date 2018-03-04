with open('movie_quotes.txt', 'r') as file:
	line = file.readline()
	
	while line != '':
		print(line, end ='') # 파이썬 3 문법이라서 이렇게 표시됨
		line = file.readline()