import os
cont = 1
filled = 0
data = []
ans = []
while cont == 1:
	ans1 = str(input("What is your FULL name?:   "))
	ans.append(ans1)
	ans2 = str(input("Who's cuter Eben Cook or Henry Lockwood?:   "))
	ans.append(ans2)
	ans3 = str(input("Who's better, Ms. Kumsen or Ms. Pashley?:   "))
	ans.append(ans3)
	ans4 = str(input("Does a minor felony charge prevent me from applying to the University of Chicago?:   "))
	ans.append(ans4)
	data.append(ans)
	cont = input("Would you like to add another data entry? 1 for yes, anything else for no.:   ")
	ans = []
	filled += 1

while filled > 0:
	print(data[filled-1])
	filled -= 1