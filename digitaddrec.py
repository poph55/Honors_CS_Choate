def digfind(n):
	sum1 = 0
	while n >= 1:
		sum1 = sum1 + n%10
		n = int(n/10)
	return sum1

sum1 = 0
n = int(input("Enter a number"))
print(digfind(n))