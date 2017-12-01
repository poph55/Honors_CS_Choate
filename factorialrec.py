def factorial(n):
	x = n - 1
	while x > 0:
		n = n * x
		x -= 1
	return n
n = int(input("Enter an umber to be factorial-ed"))
print(factorial(n))