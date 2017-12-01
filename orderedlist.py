import random

a0 = int(random.uniform(0,101))
a1 = int(random.uniform(0,101))
a2 = int(random.uniform(0,101))
a3 = int(random.uniform(0,101))
a4 = int(random.uniform(0,101))
a5 = int(random.uniform(0,101))
a6 = int(random.uniform(0,101))
a7 = int(random.uniform(0,101))
a8 = int(random.uniform(0,101))
a9 = int(random.uniform(0,101))

orderedlist = []

if a0%3 != 0:
	orderedlist.append(a0)
if a1%3 != 0:
	orderedlist.append(a1)
if a2%3 != 0: 
	orderedlist.append(a2)
if a3%3 != 0: 
	orderedlist.append(a3)
if a4%3 != 0: 
	orderedlist.append(a4)
if a5%3 != 0: 
	orderedlist.append(a5)
if a6%3 != 0: 
	orderedlist.append(a6)
if a7%3 != 0: 
	orderedlist.append(a7)
if a8%3 != 0: 
	orderedlist.append(a8)
if a9%3 != 0: 
	orderedlist.append(a9)

orderedlist.sort()

print(orderedlist)

