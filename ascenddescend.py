import sys

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

counter = 5

if y > x and z > y:
	print("True")
elif z < y and y < x:
	print("True")
else:
	print("False")
