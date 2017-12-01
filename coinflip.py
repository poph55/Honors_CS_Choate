import random
heads = 0

coinnum = int(input("How many times would you like to flip the coin?\n"))

while coinnum > 0:
	x = int(random.uniform(0,2))
	if x == 1:
		heads += 1		
	coinnum -= 1

print(heads)