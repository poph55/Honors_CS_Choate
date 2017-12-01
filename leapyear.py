val = 0
while val !=999999:
	val=int(input("Enter a year and we will tell if its a leap year."))
	donezo = not(bool(val%4))
	final = not(bool(val%100))
	kablam = not(bool(val%400))

	zippy = not (final and not kablam)
	complet = zippy and donezo

	print(complet)