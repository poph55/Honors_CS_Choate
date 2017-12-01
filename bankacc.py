import random
import sys
import os

class Account:
	def __init__(self,name):
		self.accnum = rand.uniform(100000,1000000)
		self.intrate = .004
		self.pin = 1000
		self.bal = 0
		self.status = 1

	def deposit(self):
		while 1 == 1:	
			print("Enter your pin to deposit to your account, to go back type 1.\n")
			while 1 == 1:
				try:
					pincheck = str(input(""))
					break
				except:
					print("That's not a valid PIN try again.")
			if pincheck == str(self.pin):
				while 1 == 1:
					try:
						damount = int(input())
						break
					except:
						print("That's not a number! Try again!")
					self.balance += damount
					print("You have withdrawn " + damount + " from your account. Your balance is now " + self.balance + ".\n")
			elif pincheck == '1':
				break
			else:
				print("Incorrect PIN.")



	def withdraw(self):	
		while 1 == 1:	
			print("Enter your pin to withdraw from your account, to go back type 1.\n")
			while 1 == 1:
				try:
					pincheck = str(input(""))
					break
				except:
					print("That's not a valid PIN try again.")
			if pincheck == str(self.pin):
				while 1 == 1:
					try:
						wamount = int(input())
						break
					except:
						print("That's not a number! Try again!")
					self.balance -= wamount
					print("You have withdrawn " + wamount + " from your account. Your balance is now " + self.balance + ".\n")
			elif pincheck == '1':
				break
			else:
				print("Incorrect PIN.")


	def close(self):
		while 1 == 1:	
			print("Enter your pin to close your account, to go back type 1.\n")
			while 1 == 1:
				try:
					pincheck = str(input(""))
					break
				except:
					print("That's not a valid PIN try again.")
			if pincheck == str(self.pin):
					print("You have closed your account. Goodbye.")
					sys.exit()
					os.system('clear')
			elif pincheck == '1':
				break
			else:
				print("Incorrect PIN.")

myacc1 =

while 1 == 1:
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







