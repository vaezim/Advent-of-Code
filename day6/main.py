
with open('input.txt', 'r+') as file:
	text = file.read()[:-1]

for i in range(len(text)):
	win = text[i:i+4]
	if len(set(win)) == 4:
		print(win)
		print(i+4)
		break

for i in range(len(text)):
	win = text[i:i+14]
	if len(set(win)) == 14:
		print(win)
		print(i+14)
		break