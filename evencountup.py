x = int(input("Enter a number and we will give you all even numbers lower than it! \n"))
while x != 0:
	print(x)
	if x%2 == 0:
		x -= 2
	else:
		x -= 1
		