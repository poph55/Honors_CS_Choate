import random


num1 = int(random.uniform(0,101))
num2 = int(random.uniform(0,101))
num3 = int(random.uniform(0,101))
num4 = int(random.uniform(0,101))
num5 = int(random.uniform(0,101))

list1 = [num1, num2, num3, num4, num5]

print(list1)

minimum = min(list1)
maximum = max(list1)

print(maximum, minimum)

avg = (num1+num2+num3+num4+num5)/ len(list1)

print(avg)


