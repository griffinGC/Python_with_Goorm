lines = ['안녕하세요?\n','こんにちは\n','Hello\n']

with open('greetings_utf8.txt','w',encoding='utf-8') as file:
	for i in lines:
		file.write(i)