class Argonian:
	def __init__(self, name):
		self.name = name
		self.hunger = 50
		self.thirst = 50
		self.obedience = 50
		self.health = 50
		self.lockpicking = 50
		self.intelligence = 50
		self.werecrocodile = 0

	def stats(self):
		print("Argonian stats:")
		print("Name:          " + str(self.name))
		print("Hunger:        " + str(self.hunger))
		print("Thirst:        " + str(self.thirst))
		print("Obedience:     " + str(self.obedience))
		print("Health:        " + str(self.health))
		print("Lockpicking:   " + str(self.lockpicking))
		print("Intelligence:  " + str(self.intelligence))
		print("Werecrocodile: " + str(self.werecrocodile), end = "\n\n")


	def fetch(self):
		self.health -= 5
		self.obedience += 5
		self.hunger -= 5
		self.thirst -= 7

	def lycanthropy(self):
		self.health += 30
		self.obedience -= 5
		self.hunger -= 5
		self.intelligence -= 5 
		self.werecrocodile = 1

	def lockpick(self):
		self.obedience += 5
		self.intelligence += 5
		self.lockpicking += 10
		self.health -= 5

	def study(self):
		self.obedience -= 5
		self.intelligence += 10
		self.lockpicking += 5
		self.thirst -= 5
		self.health -= 5

	def rest(self):
		self.health += 10
		self.intelligence -= 1
		self.thirst -= 1
		self.hunger -= 1
		self.lockpicking -= 1
		self.obedience -= 1

	def eat(self):
		self.health += 5
		self.hunger += 10
		self.thirst += 10
		self.intelligence -= 2
		self.lockpicking -= 2
		self.obedience -= 1

name = str(input("What would you like to name your dirty Argonian? \n"))
myarg1 = Argonian(name)


while 1 == 1 and myarg1.health > 0 and myarg1.hunger > 0 and myarg1.thirst > 0 and myarg1.obedience > 0 and myarg1.intelligence > 0:
	print("What would you like to do with your pet Argonian, " + name + "?\n")
	print("1. Fetch\n2. Lycanthropy\n3. Lockpick\n4. Study\n5. Rest\n6. Eat")
	while 1 == 1:
		try:
			choice = int(input())
			break
		except:
			print("That' not a number! Try again!")
	if choice == 1:
		myarg1.fetch()
	if choice == 2:
		myarg1.lycanthropy()
	if choice == 3:
		myarg1.lockpick()
	if choice == 4:
		myarg1.study()
	if choice == 5:
		myarg1.rest()
	if choice == 6:
		myarg1.eat()

	if myarg1.intelligence >= 100 and myarg1.lockpicking >= 100:
		print("Congratulations! Your Argonian is superbly trained! You win!")
		break
	myarg1.stats()
	print("\n \n")


if myarg1.health <= 0 or myarg1.hunger <= 0 or myarg1.thirst <= 0 or myarg1.obedience <= 0 or myarg1.intelligence <= 0:
	print("You killed your Argonian, try harder next time!")










