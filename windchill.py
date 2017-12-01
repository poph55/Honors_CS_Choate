import sys

print(sys.argv[1])
print(sys.argv[2])

if (int(sys.argv[1]) > -50 and int(sys.argv[1]) <50) and (int(sys.argv[2]) > 3 and int(sys.argv[2]) <120):
	windchill = 35.74 + (0.6215 * float(sys.argv[1])) + (0.4275 * float(sys.argv[1]) - 35.75) * (float(sys.argv[2])** (.16))	
	print(windchill)
else:
	print("Error, values are no good naughty boy,,,,,!")

