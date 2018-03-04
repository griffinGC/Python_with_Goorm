lines=["we'll find a way we always have - Interstellar\n", "I'll find you and I'll kill you - Taken\n", "I'll be back - Terminator2\n"]

with open('movie_quotes.txt', 'w') as file:
	for i in lines:
		file.write(i)
		print(i)