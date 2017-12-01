import sys

d = int(sys.argv[1])
m = int(sys.argv[2])
y = int(sys.argv[3])

y1 = y - (14-m)//12
x = y1 + y1//4 - y1//100 + (y1//400)
m1 = m + 12*((14-m)//12)-2
d1 = ((d + x + (31*m1)//12)) % 7

print(d1)

if d1 == 0:
	print("Sunday")
elif d1 == 1:
	print("Monday")
elif d1 == 2:
	print("Tuesday")
elif d1 == 3:
	print("Wednesday")
elif d1 == 4:
	print("Thursday")
elif d1 == 5:
	print("Friday")
elif d1 == 6:
	print("Saturday") 