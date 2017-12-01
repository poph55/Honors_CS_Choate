count = int(input("What digit of the Fibonacci Sequence would you like to know \n"))
num1 = 0
num2 = 1
counter = 1
final = 0

while counter != count:
	final = num1 + num2
	num1 = num2
	num2 = final
	counter += 1
print(final)
