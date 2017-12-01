import random

randnum = int(random.uniform(1,11))

guess = int(input("Enter your guess between 1-10 \n"))
print(randnum)

if guess == randnum:
	print("Correct")
else:
	print("Wrong")