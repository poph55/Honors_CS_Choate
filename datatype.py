a = 1
b = 2

def sub(a,b):
	while 1 == 1:
		a = input("Enter the first number")
		b = input("Enter the second number")
		try:
			return int(a) - int(b)
		except ValueError:
			return "Wrong data type"

print(sub(a,b))