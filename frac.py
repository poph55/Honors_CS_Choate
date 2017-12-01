class RationalNumber:
	def __init__(self,n,d):
		self.n = n
		self.d = d

	def __add__(self,other):
		n = self.n * other.d + other.n * self.d
		d = other.d * self.d
		return RationalNumber(n,d)

	def __sub__(self,other):
		n = self.n * other.d - other.n * self.d
		d = other.d * self.d
		return RationalNumber(n,d)

	def __mul__(self,other):
		n = self.n * other.n
		d = self.d * other.d
		return RationalNumber(n,d)

	def __truediv__(self,other):
		n = self.n * other.d
		d = self.d * other.n
		return RationalNumber(n,d)

	def __str__(self):
		return str(self.n)+'/'+str(self.d)

	__repr__ = __str__

def main():
	n = RationalNumber(1,2)
	d = RationalNumber(1,3)
	print(n)
	print(d)
	print(n+d)
	print(n-d)
	print(n*d)
	print(n/d)

main()