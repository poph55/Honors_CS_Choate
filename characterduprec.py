def dupcheck(string,length):
	global final
	while length < len(string):
		if string[length] != string[length-1]:
			final.append(string[length])
		length += 1


final = []
length = 0

string = input("Enter your string here \n")
list(string)

listlen = 0 

dupcheck(string,length)

while listlen < len(final):
	if listlen >= len(final):
		break
	print(final[listlen] +'', end='')
	listlen += 1

print('\n\n')