import random

birth = int(input("is it your birthday? (1 or 0)\n"))

speed = input("how fast were you going?\n")

if speed == 'idk':
	speed = int(random.uniform(30,121))
speed = int(speed)
speedval = 100
speedval2 = 80
speedval3 = 60

if birth == int(1):
	speedval = 105
	speedval2 = 85
	speedval3 = 65

print(speed)
if speed > speedval:
	print("big boy ticket")
elif speed >  speedval2:
	print("small boy ticket")
else: 
	print("goodboy")