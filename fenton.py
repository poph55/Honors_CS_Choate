'''
All of the code is my own, but I was taught how to use the time.sleep function by Henry. 
If I had more time, I would also liked to have made a function to print strings then ask the user to press enter to continue. 
I didn't realize at first how often I would be using that function, but by the time I realized, it was effectively too late to remake those parts of the game as functions. 
My other functions, however, I think are excellent. They are super customizable, but I had to use some weird techniques by making every variable global

'''

import os
import sys
import random
import time

######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################

def fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstr, playerint, playerspd):
	
	global playerstrcurrent
	global playerintcurrent
	global playerspdcurrent
	global playerhpcurrent

	print("-~~~------------------------!~~~-FIGHT START-~~~!---------------------~~~-")
	while enemyhp > 0 and playerhpcurrent > 0: #this ensures that when either the player or the enemy reaches 0 hp, the fight ends.
		print("     " + enemyname + ": " + str(enemyhp) + "         " + playername + ": " + str(playerhpcurrent) + "\n") #this prints the hp of both fighters
		print(" 1: Dropkick             2: Mind Blast      \n") #this prints the attack options
		if newattackchoice1 == '1': #the following few lines print the attacks you have learned based on what you choose.
			print(" 3: Velocity Strike     ", end='')
		if newattackchoice1 == '2':
			print(" 3: Quick Thinking      ", end='')
		if newattackchoice2 == '1':
			print(" 4: Cheap Shot")
		if newattackchoice2 == '2':
			print(" 4: Seduce")
		print('\n')
		attack = str(input())
		if attack == '1': #this calculates how much damage the enemy is going to take based on what attack you choose
			enemyhploss = playerstrcurrent
		elif attack == '2':
			enemyhploss = playerintcurrent
		elif attack == '3' and newattackchoice1 == '1': #the next few lines filters the effect based on your attack choice and what move you chose to learn earlier
			enemyhploss = int(.6 * playerstrcurrent) + int(.4 * playerspdcurrent)
			playerspdcurrent += 2
		elif attack == '3' and newattackchoice1 == '2':
			enemyhploss = int(.6 * playerintcurrent) + int(.4 * playerspdcurrent)
			playerspdcurrent += 2
		elif attack == '4' and newattackchoice2 == '1':
			enemyhploss = 6
			enemyspd = enemyspd/2
		elif attack == '4' and newattackchoice2 == '2':
			enemyhploss = 2
			enemystr = enemystr/2
		else:
			print("That isn't an attack you fool!")
		playerhploss = enemystr #the player always takes damage based on the opponents strength.
		if playerspdcurrent > enemyspd: #if playerspd is higher the player goes first. If the players attack kills the enemy, the enemy does not deal damage to the player
			enemyhp = enemyhp - enemyhploss 
			if attack == '1':
				print("You slam your enemy with your meaty quads dealing " + str(enemyhploss) + " damage! \n")
			if attack == '2':
				print("You shatter the enemy's mind with your superior intellect dealing " + str(enemyhploss) + " damage! \n")
			if attack == '3' and newattackchoice1 == '1':
				print("You swiftly strike the enemy with severe force, increasing your SPD by 2 and dealing " + str(enemyhploss)+ " damage! \n")
			if attack == "3" and newattackchoice1 == '2':
				print("Your IQ of 645 allows you to outsmart your opponent, landing a powerful blow with extreme speed increasing your SPD by 2 and dealing " + str(enemyhploss) + " damage! \n")
			if attack == '4' and newattackchoice2 == '1':
				print("You hit your opponent while they are offguard, halving their SPD and dealing " + str(enemyhploss) + " damage! \n")
			if attack == '4' and newattackchoice2 == '2':
				print("Your movements hypnotize your opponent, halving their INT and STR and dealing " + str(enemyhploss) + " damage!\n")
			if enemyhp <= 0:
				break
			playerhpcurrent = playerhpcurrent - playerhploss
			print(enemyattackstring + " " + str(playerhploss) +" damage! \n")	
		else:
			playerhpcurrent = playerhpcurrent - playerhploss
			print(enemyattackstring + " " +str(playerhploss) +" damage! \n")
			if playerhpcurrent <= 0: 
				break
			enemyhp = enemyhp - enemyhploss
			if attack == '1': #the next few lines print flavor text for each of the moves you may learn throughout the game
				print("You slam your enemy with your meaty quads dealing " + str(enemyhploss) + "damage! \n")
			if attack == '2':
				print("You shatter the enemy's mind with your superior intellect dealing " + str(enemyhploss) + " damage! \n")	
			if attack == '3' and newattackchoice1 == '1':
				print("You swiftly strike the enemy with severe force, increasing your SPD by 2 and dealing " + str(enemyhploss)+ " damage! \n")
			if attack == "3" and newattackchoice1 == '2':
				print("Your IQ of 645 allows you to outsmart your opponent, landing a powerful blow with extreme speed increasing your SPD by 2 and dealing " + str(enemyhploss) + " damage! \n")
			if attack == '4' and newattackchoice2 == '1':
				print("You hit your opponent while they are offguard, halving their SPD and dealing " + str(enemyhploss) + " damage! \n")
			if attack == '4' and newattackchoice2 == '2':
				print("Your movements hypnotize your opponent, halving their INT and STR and dealing " + str(enemyhploss) + " damage!\n")
	if enemyhp <= 0:
		print("Congratulations! You won the fight! \n      Your rewards are: " + enemyloot +", " + str(enemyexp) +" Experience Points (EXP)!")
	elif playerhpcurrent <= 0:
		print("-----------------!!!!~~~ GAME OVER ~~~!!!!-----------------")
		sys.exit()
		os.system('clear')
	input("Press Enter to continue!")
	global playerexp
	playerexp = playerexp + int(enemyexp)
	playerinv.append(enemyloot)
	os.system('clear')

######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################

def inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine):

	#Stats are calculated as a base value + value given by items. Below, all of the value given by item variables are set as global.
	#I also made current stats which are important for moves that increase your stats temporarily. This allows me to change stats mid-battle without making permanent changes.
	global weaponstr
	global weaponint
	global weaponspd
	global weaponhp

	global helmstr
	global helmint
	global helmspd
	global helmhp

	global cheststr
	global chestint
	global chestspd
	global chesthp

	global bootstr
	global bootint
	global bootspd
	global boothp

	global playerstrcurrent
	global playerintcurrent
	global playerspdcurrent
	global playerhpcurrent

	global playerexp
	global playerlvl
	global playerstr
	global playerint
	global playerspd
	global playerhpmax

	playerstrcurrent = playerstr
	playerintcurrent = playerint
	playerspdcurrent = playerspd
	playerhpcurrent = playerhpmax

	#Below Character equipped items and stats are equipped along with stats so players know what they have 
	print("~~~~CHARACTER~~~~")

	print('Weapon: ' + equippeditems[0])
	print('Helm:   '+ equippeditems[1])
	print('Chest:  '+ equippeditems[2])
	print('Boots:  ' + equippeditems[3])

	print("~~~~~STATS~~~~~")
	print("LVL: " + str(playerlvl))
	print("STR: " + str(playerstrcurrent + weaponstr + helmstr + cheststr + bootstr))
	print("INT: " + str(playerintcurrent + weaponint + helmint + chestint + bootint))
	print("SPD: " + str(playerspdcurrent + weaponspd + helmspd + chestspd + bootspd))
	print("HP:  " + str(playerhpcurrent + weaponhp + helmhp + chesthp + boothp))

	print("~~~INVENTORY~~~")

	#below is the code that gives players the ability to equip certain items, or examine the items to see what they do 
	#The equip function first checks where the item should be equipped, then equips it, altering the item stats accordingly
	#the examine function simply prints some flavorful text about the item, and what stats the item provides

	item = 1
	totalitems = len(playerinv)
	while item <= totalitems:
		print(str(item) +": " + playerinv[item-1])
		item += 1 
	while invchoice != '4':
		print("\n1: Equip an item\n2: Examine an item\n3: Refresh equipped items\n4: Exit")
		invchoice = input()
		while invchoice == '1':
			print("Enter the number of the item in your inventory you would like to equip. To go back to the previous menu enter '0'")
			while 1 == 1:
				try:
					equip = int(input())
					break
				except:
					print("That' not a number! Try again!")
			if (equip > 0 and equip <= len(playerinv)):
				print("You equipped the " + playerinv[equip-1])
				if playerinv[equip-1] == 'Sharpened Tusk' or playerinv[equip-1] == 'Handle-Worn Axe' or playerinv[equip-1] == 'Scantily Clad Wand' or playerinv[equip-1] == 'Demi-God Staff' or playerinv[equip-1] == 'Spirit-Infused God Staff':
					equippeditems[0] = playerinv[equip-1]
					if equippeditems[0] == 'Nothing':
						weaponstr = 0
						weaponint = 0
						weaponspd = 0
						weaponhp = 0
					if equippeditems[0] == 'Sharpened Tusk':
						weaponstr = 2
						weaponint = 2
						weaponspd = 0
						weaponhp = 0
					if equippeditems[0] == 'Handle-Worn Axe':
						weaponstr = 5
						weaponint = -2
						weaponspd = 0
						weaponhp = 5
					if equippeditems[0] == 'Scantily Clad Wand':
						weaponstr = 0
						weaponint = 9
						weaponspd = 6
						weaponhp = 0
					if equippeditems[0] == 'Demi-God Staff':
						weaponstr = 15
						weaponint = 15
						weaponspd = 15
						weaponhp = 15
					if equippeditems[0] == 'Spirit-Infused God Staff':
						weaponstr = 100
						weaponint = 100
						weaponspd = 100
						weaponhp = 100

				if playerinv[equip-1] == 'Worn Leather Helmet' or playerinv[equip-1] == 'Propeller Hat' or playerinv[equip-1] == 'Iron-Horned Helmet':
					equippeditems[1] = playerinv[equip-1]
					if equippeditems[1] == 'Nothing':
						helmstr = 0
						helmint = 0
						helmspd = 0
						helmhp = 0
					if equippeditems[1] == 'Worn Leather Helmet':
						helmstr = 0
						helmint = 0
						helmspd = 0
						helmhp = 3
					if equippeditems[1] == 'Propeller Hat':
						helmstr = 0
						helmint = 0
						helmspd = 7
						helmhp = 4
					if equippeditems[1] == 'Iron-Horned Helmet':
						helmstr = 15
						helmint = 0
						helmspd = 5
						helmhp = 5

				if playerinv[equip-1] == 'Sturdy Leather Jacket' or playerinv[equip-1] == "'Children's Medium' Cape of Fear" or playerinv[equip-1] == 'Chest-Mounted Mind Control Laser Raven':
					equippeditems[2] = playerinv[equip-1]
					if equippeditems[2] == 'Nothing':
						cheststr = 0
						chestint = 0
						chestspd = 0
						chesthp = 0
					if equippeditems[2] == 'Sturdy Leather Jacket':
						cheststr = 1
						chestint = 1
						chestspd = 0
						chesthp = 3
					if equippeditems[2] == "'Children's Medium' Cape of Fear":
						cheststr = 0
						chestint = 0
						chestspd = 5
						chesthp = 7
					if equippeditems[2] == 'Chest-Mounted Mind Control Laser Raven':
						cheststr = 0
						chestint = 15
						chestspd = 5
						chesthp = 5

				if playerinv[equip-1] == 'Chewed-up Shoes' or playerinv[equip-1] == 'Water Otter Trotters' or playerinv[equip-1] == 'Fuzzy Slippers' or playerinv[equip-1] == "Naruto's Shoes":
					equippeditems[3] = playerinv[equip-1]
					if equippeditems[3] == 'Nothing':
						bootstr = 0
						bootint = 0
						bootspd = 0
						boothp = 0
					if equippeditems[3] == 'Chewed-up Shoes':
						bootstr = 0
						bootint = 0
						bootspd = 3
						boothp = 1
					if equippeditems[3] == 'Water Otter Trotters':
						bootstr = 0
						bootint = 0
						bootspd = 7
						boothp = 2
					if equippeditems[3] == 'Fuzzy Slippers':
						bootstr = -1
						bootint = -1
						bootspd = 7
						boothp = 10
					if equippeditems[3] == "Naruto's Shoes":
						bootstr = 2
						bootint = 2
						bootspd = 13
						boothp = 8

			elif equip == 0:
				invchoice ==''
				break
			else:
				print("That doesn't correspond to an item in your inventory, try again.")
		while invchoice == '2':
			print("Enter the number of the item in your inventory you would like to examine. To go back to the previous menu enter '0'")
			while 1 == 1:
				try:
					examine = int(input())
					break
				except:
					print("That's not a number! Try again")
			if examine  > 0 and examine <= len(playerinv):
				if playerinv[examine-1] == 'Sharpened Tusk':
					print("The Sharpened Tusk grants 2 STR and 2 INT!")
				if playerinv[examine-1] == 'Worn Leather Helmet':
					print("The Worn Leather Helmet grants 3 HP!")
				if playerinv[examine-1] == 'Sturdy Leather Jacket':
					print("The Jacket Bolsters your confidence, giving you 3 HP, 1 STR, and 1 INT!")
				if playerinv[examine-1] == 'Chewed-up Shoes':
					print("The ruined shoes make you feel mobile, giving you 3 SPD and 1 HP!")
				if playerinv[examine-1] == 'Handle-Worn Axe':
					print("For some reason it looks like whoever used this before hit things with the handle... It still grants 5 STR, 5 HP, but decreases INT by 2!")
				if playerinv[examine-1] == 'Water Otter Trotters':
					print("These shoes seem to have been stolen from a magical aquatic otter who blesses you with 7 SPD and 2 HP!")
				if playerinv[examine-1] == "'Children's Medium' Cape of Fear":
					print("The cape barely fits! It must have been worn by a very small, very sad man. Nevertheless, it grants 5 SPD and 7 HP!")
				if playerinv[examine-1] == 'Fuzzy Slippers':
					print("The shoes have only been worn once or twice, the innocent owner must have recently received them as a gift from their loving father. The guilt they remind you of decreases your STR by 1 and INT by 1. On the other hand, the cozy lining increases your SPD by 7 and your HP by 10!")
				if playerinv[examine-1] == 'Propeller Hat':
					print("This hat spins pretty! It also grants 7 SPD and 4 HP!")
				if playerinv[examine-1] == 'Scantily Clad Wand':
					print("The wand stares at you provocatively granting 9 INT and 6 SPD!")
				if playerinv[examine-1] == 'Chest-Mounted Mind Control Laser Raven':
					print("John Bird's signature tool. Without this he is powerless. You, however, may harness its power. It grants 15 INT, 5 SPD, and 5 HP!")
				if playerinv[examine-1] == 'Iron-Horned Helmet':
					print("Henry Lockleer's signature tool. Without this he is powerless. You, however, may harness its power. It grants 15 STR, 5 SPD, and 5 HP!")
				if playerinv[examine-1] == "Naruto's Shoes":
					print("Sea-Bastion's signature tool. Without these he is powerless. You, however, may harness its power. It grants 2 STR, 2 INT, 13 SPD, and 8 HP!")
				if playerinv[examine-1] == 'Demi-God Staff':
					print("The Z-nomorph's life force is sealed in the staff. It provides you with magical essence, increasing all of your stats by 15!")	
				if playerinv[examine-1] == 'Spirit-Infused God Staff':
					print("The King's spirit is infused directly into the already powerful staff. It fills your body with profound energy, increasing all of your stats by 100!")		
			elif examine == 0:
				invchoice =='1000'
				break
			else:
				print("That number doesn't correspond to an item in your inventory, try again.")
		if invchoice == '3':
			os.system('clear')

			print("~~~~CHARACTER~~~~")

			print('Weapon: ' + equippeditems[0])
			print('Helm:   ' + equippeditems[1])
			print('Chest:  ' + equippeditems[2])
			print('Boots:  ' + equippeditems[3])

			print("~~~~~STATS~~~~~")

			print("LVL: " + str(playerlvl))
			print("STR: " + str(playerstrcurrent + weaponstr + helmstr + cheststr + bootstr))
			print("INT: " + str(playerintcurrent + weaponint + helmint + chestint + bootint))
			print("SPD: " + str(playerspdcurrent + weaponspd + helmspd + chestspd + bootspd))
			print("HP:  " + str(playerhpcurrent + weaponhp + helmhp + chesthp + boothp))

			item = 1
			print("~~~INVENTORY~~~")
			while item <= totalitems:
				print(str(item) +":   " + playerinv[item-1])
				item += 1 
		if invchoice =='4':
			break
		if invchoice != '4' and invchoice != '3' and invchoice != '2' and invchoice != '1':
			print("That isn't an option!")
	os.system('clear')

	playerstrcurrent = playerstr + weaponstr + helmstr + cheststr + bootstr
	playerintcurrent = playerint + weaponint + helmint + chestint + bootint
	playerspdcurrent = playerspd + weaponspd + helmspd + chestspd + bootspd
	playerhpcurrent = playerhpmax + weaponhp + helmhp + chesthp + boothp

	#If the playerexp is higher than 100, the players exp is decreased by 100, their level goes up by 1, and they get to increase a stat by 2. 
	#If the player enters numbers that are not mapped to stats, they do not get a stat bonus. I filtered options above, but I want to punish players for disobeying me

	if playerexp >= 100:
		playerlvl += 1 
		print("Woah you Leveled up! You are now level " + str(playerlvl) + "! Pick which stat you want to increase by 2!")
		print(" 1) STR: " + str(playerstrcurrent))
		print(" 2) INT: " + str(playerintcurrent))
		print(" 3) SPD: " + str(playerspdcurrent))
		print(" 4) HP:  " + str(playerhpcurrent))
		while 1 == 1:
			try:
				levelup = int(input())
				break
			except:
				print("That's not a number! Try again!")
		if int(levelup) == 1:
			playerstr += 2
			playerstrcurrent = playerstr + weaponstr + helmstr + cheststr + bootstr
			print("Your Strength is now " + str(playerstrcurrent))
		elif int(levelup) == 2:
			playerint += 2
			playerintcurrent = playerint + weaponint + helmint + chestint + bootint
			print("Your Intelligence is now " + str(playerintcurrent))
		elif int(levelup) == 3:
			playerspd += 2
			playerspdcurrent = playerspd + weaponspd + helmspd + chestspd + bootspd
			print("Your Speed is now " + str(playerspdcurrent))
		elif int(levelup) == 4:
			playerhpmax += 2
			playerhpcurrent = playerhpmax + weaponhp + helmhp + chesthp + boothp
			print("Your HP is now " + str(playerhpcurrent))
		else:
			print("I guess you don't want extra stats... fine by me.")
		playerexp = playerexp - 100

######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################

'''#### ITEM INFORMATION ####'''

equippeditems = ['Nothing','Nothing','Nothing','Nothing']
item = 0
totalitems = 0
playerinv = []
equip = ''
examine = ''

itemindex = []

invchoice = '1000'

weaponstr = 0
weaponint = 0
weaponspd = 0
weaponhp = 0

helmstr = 0
helmint = 0
helmspd = 0
helmhp = 0

cheststr = 0
chestint = 0
chestspd = 0
chesthp = 0

bootstr = 0
bootint = 0
bootspd = 0
boothp = 0

'''#### ITEM INFORMATION ####'''



'''#### PLAYER STATS ####'''
playerlvl = 1
playerstr = 5
playerint = 5
playerspd = 5
playerhpmax = 10

playerstrcurrent = playerstr
playerintcurrent = playerint
playerspdcurrent = playerspd
playerhpcurrent = playerhpmax
playerexp = 0
newattackchoice1 = 0
newattackchoice2 = 0
'''#### PLAYER STATS ####'''



'''#### PLAYERCURRENT STATS - HEAL ####'''

playerstrcurrent = playerstr
playerintcurrent = playerint
playerspdcurrent = playerspd
playerhpcurrent = playerhpmax

'''#### PLAYERCURRENT STATS - HEAL ##### '''

os.system('clear')

print("------------------------------GAME START------------------------------")
print("You wake up on the beach to find a burly man looking you over... \n\n'What are you doing here?' he says. 'You look ill, let me take you to the inn' \nHe picks you up with his muscular quadraceps and takes you to get medical care.")

playername = str(input("What is your name young one?\n"))

os.system('clear')

print("'Ah, hello young " + playername + ", my name is Jack Fenton!'")

print("\n'These potions will heal you, " + playername + "' he says. 'Drink 5 and then call for me' \nThe potions lie before you.")

print("Press 1 to drink Hungry Lockleer's Potion of Strength. \nPress 2 to drink Sea-Bastion Chang's Potion of Speed \nPress 3 to drink John Bird's Potion of Intelligence \nPress 4 to drink Jack Fenton's Potion of Fortitude \n ")


potioncounter = 0

while potioncounter < 5:
	currentpotion = str(input("What potion would you like to drink next?"))
	if currentpotion == '1':
		playerstr += 2
		print("Your strength went up by 2, it is now " + str(playerstr) + "!")
	elif currentpotion == '2':
		playerspd += 2 
		print("Your speed went up by 2, it is now " + str(playerspd) + "!")
	elif currentpotion == '3':
		playerint += 2
		print("Your intelligence went up by 2, it is now " + str(playerint) + "!")
	elif currentpotion == '4':
		playerhpmax	+= 2 
		print("Your Health went up by 2, it is now " + str(playerhpmax) + "!")
	else:
		print("You reach for Jack Fenton's throbbing bicep. 'No! The potions you dunce!'")
		potioncounter -= 1
	potioncounter += 1
	currentpotion=0

playerstrcurrent = playerstr
playerintcurrent = playerint
playerspdcurrent = playerspd
playerhpcurrent = playerhpmax

os.system('clear')
print("LVL: " + str(playerlvl) + "\nSTR: "+ str(playerstr) + "\nINT: " + str(playerint) + "\nSPD: " + str(playerspd) + "\nHP:  " + str(playerhpmax) + "\n")

print("Jack Fenton sets down his weights and turns to you...'Are you ready for your first fight, " +playername +"?'")
input()
os.system('clear')
print("'I don't particularly care!' bellows Jack Fenton, releasing a boar from the pen beside him!")

#For every fight, I only have to redefine some of the enemy stats, including their name and attack text. As well as the EXP they give and the loot they drop. 
#This is all filtered through the fightstart function and processed by the inventory function. Because of this, creating new battle sequences in the game was very easy.


'''#### ENEMY STATS ####'''

enemyname = 'Boar'
enemyhp=10
enemystr=6
enemyint=6
enemyspd=6
enemyhploss = 0
enemyattackstring='The boar slams you with its tusks dealing'
enemyloot = 'Sharpened Tusk'
enemyexp = 100
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)

print("Jack Fenton runs to your side, 'Let me heal you up!' he says, not seeming particularly concerned. \n'Good work, " + playername +". You did wonderfully! Let me heal you up!'")
input("Press Enter to continue!")
os.system('clear')

print("'After every fight you will have the opportunity to check your inventory to look at your most recent loot.'\n'Why don't you check it out?'")
input("Press Enter to continue!")
os.system('clear')

inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)
input("Press Enter to continue!")
os.system('clear')

print("'Everything went well I imagine? Oh Goodness! You leveled up already! Well I'm sure you have figured out how leveling up works by now...'")
input("Press Enter to continue!")
os.system('clear')

print("'Now that you are SoOoOoOoOo powerful, I think I should teach you a new attack!'")
input("Press Enter to continue!")
os.system('clear')

print("Jack Fenton is offering to teach you one of two different moves! How exciting! \n1) Velocity Strike - Deal damage equal to 60'%' of your STR and 40'%' of your SPD, increases speed by 2\n OR\n2) Quick Thinking - Deal damage equal to 60'%' of your INT and 40'%' of your SPD, increases speed by 2\n")
newattackchoice1 = str(input("What will it be?"))

while newattackchoice1 != '1' and newattackchoice1 != '2':
	print("Are you blind? That wasn't a choice?!")
	newattackchoice1 = str(input())

print("Congratulations on your new attack! Use it wisely!")
input("Press Enter to continue!")
os.system('clear')

print("'Uh-oh. We should get out of here, I can hear the trolls marching towards us.'")
input("Press Enter to continue!")
os.system('clear')

print("'The trolls?' You say, equally concerned and afraid.")
input("Press Enter to continue!")
os.system('clear')

print("'Yeah, y'know that movie Trolls 2, it's basically that. That's kinda what we're dealing with' says Jack Fenton, looking more terrified with every word, the beads of sweat collecting on his burly forearms.")
input("Press Enter to continue!")
os.system('clear')

print("'Oh, of course.' you say, completely understanding the context and nuance of the situation you have been thrust into.")
input("Press Enter to continue!")
os.system('clear')

print("'Here comes one of the trolls!!!' says Jack, 'Get him, " +playername +"!'")
input("Press Enter to continue!")
os.system('clear')

'''#### ENEMY STATS ####'''

enemyname = 'Troll Grunt'
enemyhp=16
enemystr=4
enemyint=8
enemyspd=8
enemyhploss = 0
enemyattackstring='The troll yells or something, but in a painful way dealing'
enemyloot = 'Worn Leather Helmet'
enemyexp = 60
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

print("'Wait, that was actually pretty tubular, you're almost as strong as me already;")
input("Press Enter to continue!")
os.system('clear')

print("'We have a ways to go, " + playername +", we should be on our way.'")
input("Press Enter to continue!")
os.system('clear')

print("As you climb upwards, the hill you were climbing before becomes a mountain, and then a tower. As you approach the cloudline, you see what used to be the village Jack Fenton had lived in. You see the beach where you were first found. It all seems so familiar, but you can't place where you have seen it before.")
input("Press Enter to continue!")
os.system('clear')

print("You come across what appears to be some sort of ancient temple. The ruins of a statue sit silently in the middle of the courtyard. Two lone trunks, no longer supporting the torso they were built for.")
input("Press Enter to continue!")
os.system('clear')

print("On the cliff on the rear of the temple you sit with Jack Fenton. He begins to reminisce about his now destroyed home. -'I've been training for this day since my youth, and I still couldn't defend my home'")
input("Press Enter to continue!")
os.system('clear')

print("'This isn't the end, I won't give up! We should go to the Capitol and enlist the help of the Queen's Army, that will surely help.'")
input("Press Enter to continue!")
os.system('clear')

print("You agree to go with Jack Fenton, he seems to need help, and so do you. Your past is muddied, but slowly revealing itself, perhaps this journey will reveal some sort of divine purpose.")
input("Press Enter to continue!")
os.system('clear')

print("Suddenly, two Wyverns come circling down the towering mountain and land in front of you, they clearly are not here for a conversation.")
input("Press Enter to continue!")
os.system('clear')

'''#### ENEMY STATS ####'''

enemyname = 'Young Wyvern'
enemyhp=16
enemystr=3
enemyint=2
enemyspd=12
enemyhploss = 0
enemyattackstring='The Young Wyvern slashes you with his talons dealing'
enemyloot = 'Chewed-up Shoes'
enemyexp = 30
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)

'''#### ENEMY STATS ####'''

enemyname = 'Mama Wyvern'
enemyhp=22
enemystr=5
enemyint=8
enemyspd=14
enemyhploss = 0
enemyattackstring='The mother, furious at your slaying of her son, creates a furious gust of wind dealing'
enemyloot = 'Sturdy Leather Jacket'
enemyexp = 80
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

print("'Jesus!' said Jack. 'We better keep moving before more of those things come down for us.'")
input("Press Enter to continue!")
os.system('clear')

print("You look at the corpses of your two slain foes and see a circular golden coin hanging from what looks like a collar. The letters JB are inscribed on the front and the letters QC are engraved on the back. You think nothing of it and continue following Jack. This is his mission after all.")
input("Press Enter to continue!")
os.system('clear')



print("You and Jack reach an intersection, to your right lies a dimly lit cave that seems to wind upwards. On the left, the mountain continues, but appears more treacherous than before. Which way would you like to go?\n1) Right\n2) Left ")
rl = input('')
while rl != '1' and rl != '2':
	rl = input("That isn't an option!")
input("Press Enter to continue!")
os.system('clear')


if rl == '1':
	print("You have chosen to go to the right, into the dimly lit cave. Jack says,'This seems like the safest way to go!'")
	input("Press Enter to continue!")
	os.system('clear')

	print("You walk deeper into the cave. Small piles of bones begin to form on your sides as you walk deeper. The piles turn to mounds and the mounds to mountains until you can hardly see the cave walls.")
	input("Press Enter to continue!")
	os.system('clear')

	print("Before you have an opportunity to regret your decision, an axe-wielding Ogre appears behind you. You try to run forwards, but a mound of bones crashes down, blocking your path. There is no choice but to fight.")
	input("Press Enter to continue!")
	os.system('clear')

	'''#### ENEMY STATS ####'''

	enemyname = 'Axe-Wielding Ogre'
	enemyhp=46
	enemystr=4
	enemyint=8
	enemyspd=6
	enemyhploss = 0
	enemyattackstring='The Ogre flails the handle of his axe in your direction dealing'
	enemyloot = 'Handle-Worn Axe'
	enemyexp = 100
	attack='0'
	playerhploss = 0

	'''#### ENEMY STATS ####'''

	fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
	inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

	print("You continue on through the cave, slowly progressing until you see the exit which places you near the summit; near the Capitol.")
	input("Press Enter to continue!")
	os.system('clear')

if rl == '2':
	print("You have chosen to go to the left, up the treacherously winding mountain. Jack says, 'This seems like the safest way to go!")
	input("Press Enter to continue!")
	os.system('clear')

	print("As you scale the mountain you reach a small ledge where you can safely rest. You notice a small opening in the rocks that leads to a pool. You decide to go there to briefly rest. As you bend down to get a drink of water a mysterious figure appears before you! 'It's the Aqua Wizard Lizard!' yells Jack.")
	input("Press Enter to continue!")
	os.system('clear')

	'''#### ENEMY STATS ####'''
	
	enemyname = 'Aqua Wizard Lizard'
	enemyhp=24
	enemystr=5
	enemyint=8
	enemyspd=14
	enemyhploss = 0
	enemyattackstring='The Wizard Lizard casts Blizzard dealing'
	enemyloot = 'Water Otter Trotters'
	enemyexp = 100
	attack='0'
	playerhploss = 0

	'''#### ENEMY STATS ####'''

	fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
	inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

	print("You leave the pond as fast as you can, hoping to avoid any other creatures with charmingly rhymed names. You continue up the mountain until you are close to the summit.")
	input("Press Enter to continue!")
	os.system('clear')

print("You can see the gates to the Capitol, and you see the delight on Jack's rosey-cheeked face.")
input("Press Enter to continue!")
os.system('clear')

print("'The Capitol!' says Jack Fenton. You run to the gates and enter the bustling city at the peak of the mountain.")
input("Press Enter to continue!")
os.system('clear')

print("The city zooms around you on all sides, something about it seems familiar, but you're not sure what exactly. Jack seems to know exactly where he is going, so you follow him.")
input("Press Enter to continue!")
os.system('clear')

print("You make your way through the labrynth of the city and finally reach a second monstrous gate. 'This leads to the inner sanctum.' says Jack. 'That is where the Queen is.'")
input("Press Enter to continue!")
os.system('clear')

print("The process required to get a meeting with the Queen is not so simple, but Jack spares you the worry and completes the task himself as you relax and enjoy yourself at the local Healey-Day Inn nearby.")
input("Press Enter to continue!")
os.system('clear')

print("After several days of waiting, the day of your appointment finally arrives. You return to the illustrious gates, but this time they open for you, revealing a throne room of magnificent proportions. On the throne sits the feline Queen, Queen Connie Miao.")
input("Press Enter to continue!")
os.system('clear')

print("'For what PURRRRRRRRRRRpose do you bother me?' faintly utters the Queen.")
input("Press Enter to continue!")
os.system('clear')

print("'Your Majesty, I am Jack Fenton. My village has been under siege by the trolls for decades, but now it appears they are increasing their efforts. They have destroyed the town I once called home. We need your help to defend the countryside. Please, lend us your aid to destroy this foul threat to your kingdom!'")
input("Press Enter to continue!")
os.system('clear')

print("'The Queen takes a moment to consider and responds to Jack rather coldly, 'I admire your efforts Jack, but you seem to be giving up your struggle prematurely. You won't get anything done with that Cat-ittude.'")
input("Press Enter to continue!")
os.system('clear')

print("'Your Majesty,' begs Jack, 'I have done all I can, and I am sorry to have failed you, but we cannot defeat this threat without your help! Are you certain there is no aid you may be so gracious as to provide us?'")
input("Press Enter to continue!")
os.system('clear')

print("'Yes Jack, I am Paws-itive. Now please leave.")
input("Press Enter to continue!")
os.system('clear')

print("'Please! I beg of you!' exclaimed Jack, falling to his knees. 'I have nowhere else to turn!'")
input("Press Enter to continue!")
os.system('clear')

print("'I am sorry Jack, but no amount of Purr-suasian will change my answer.' The Queen motions to her guards. 'Take them to the dungeon! That isn't a pun either, legitimately take them to the dungeon.'")
input("Press Enter to continue!")
os.system('clear')

print("The guards grab you with too much force to resist, dragging you down a spiral staircase and throwing you in a locked cell. There is another man in the same cell as you and Jack. He doesn't seem interested in conversing at the moment.")
input("Press Enter to continue!")
os.system('clear')

print("You spend the next several days in the cell. There is no sunlight, and your health feels drained, but you keep fighting, hoping for some end to your torment.")
input("Press Enter to continue!")
os.system('clear')

print("On the 7th day, the man finally speaks to you. 'Who are you,' he says, 'I think I know you.' You turn around startled, never having seen this man before in your life. 'I am " + playername + ".' you say.")
input("Press Enter to continue!")
os.system('clear')

print("'Interesting' says the man calmly.")
input("Press Enter to continue!")
os.system('clear')

print("The man does not speak again until the 18th day. 'I knew a " + playername + " before. He disappeared several years ago.'")
input("Press Enter to continue!")
os.system('clear')

print("You press the man for more information about the disappearing man, perhaps he is speaking of you and does not know it! But the man refuses to speak.")
input("Press Enter to continue!")
os.system('clear')

print("On the 43rd day the man speaks for the third time. 'There is a reason the King is no longer around... The King had several bastard children. This upset the Queen greatly. He was ousted long ago, but his legacy lives on in those children. There are four of them. You, " + playername +" are one. The other three were not as lucky as you. They have been afflicted by the Queen's spell. She has lived her life full of spite for her husbands actions. She exacts her revenge by draining the power of those children. They are now her closest advisors. You may have heard of them before. Hungry Lockleer, John Bird, and The Sea-Bastion. These are their names.'")
input("Press Enter to continue!")
os.system('clear')

print("'What does this mean!'' you press, 'What am I supposed to do with this vague, cryptic information!'")
input("Press Enter to continue!")
os.system('clear')

print("The man refuses to speak again")
input("Press Enter to continue!")
os.system('clear')

print("The 84th day arrives and the man seems prepared to tell you more, 'My days are numbered, friends. I must tell you all I know. My name is Grievous the Revenant, I faked my death to save you, " + playername + ". To snatch you from your crib before the Queen worked her magic on you. The King has left to the Other-World, but you are still here. You must slay your siblings and overthrow the corrupt regime of Connie Miao. She is the one who has sent the trolls to the village, she is looking for you. Find your siblings, and kill them. This will weaken Connie so that you may fight her without facing certain death. The oppressive regime of Connie Miao must be stopped at once! Viva La Revolucion!'")
input("Press Enter to continue!")
os.system('clear')

print("The man croaks dead, exploding into a cloud of ash.")
input("Press Enter to continue!")
os.system('clear')

print("In the place of the dead man's body lies a puddle. The puddle does not show you your reflection when you stand over it, however, and you examine more closely.")
input("Press Enter to continue!")
os.system('clear')

print("You quickly dip your finger in it, and find it is deeper than it appears, in fact, it seems to go on as far as you can reach. You take the leap of faith and find yourself fall from the cieling of a rather similar cellar. You go up the stairs to find the door unlocked, and you make your escape.")
input("Press Enter to continue!")
os.system('clear')

print("You open the door to find a rather angry looking Goblin! 'I'm not a Goblin, I'm just short!' yells the Goblin. You must slay the Goblin. 'Oh, oh God please I'm not a threat, you can pass me by, just please don't hurt me.' says the Goblin threateningly.")
input("Press Enter to continue!")
os.system('clear')

print("When you attack the Manlet, his body slowly grows, and scales begin to grow around his exterior forming an exoskeleton of magnificent proportions. His stubby fingers turn to claws and his sense of smell improves greatly, but that isn't a stat in the game so it doesn't really matter.")
input("Press Enter to continue!")
os.system('clear')

'''#### ENEMY STATS ####'''
	
enemyname = 'Manlet'
enemyhp=58
enemystr=4
enemyint=8
enemyspd=16
enemyhploss = 0
enemyattackstring='The Manlet fires piercing bolts from his ribcage dealing'
enemyloot = "'Children's Medium' Cape of Fear"
enemyexp = 100
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

print("'Good job! You probably forgot I was even here didn't you!' says Jack. 'Truth is, I'm very afraid. Please protect me.'")
input("Press Enter to continue!")
os.system('clear')

print("'Oh no! Here comes his son! Destroy him!' yells Jack!")
input("Press Enter to continue!")
os.system('clear')

print("'Dad?' calls the child. 'Where are you?'")
input("Press Enter to continue!")
os.system('clear')

print("You attack the child with full force")
input("Press Enter to continue!")
os.system('clear')

'''#### ENEMY STATS ####'''
	
enemyname = 'Son of Manlet'
enemyhp=5
enemystr=1
enemyint=8
enemyspd=3
enemyhploss = 0
enemyattackstring='The child sits idly. Your guilt, however, hurts more than any attack dealing'
enemyloot = "Fuzzy Slippers"
enemyexp = 10
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

print("You murder the child.")
input("Press Enter to continue!")
os.system('clear')

print("You and Jack agree not to discuss the matter in the future.")
input("Press Enter to Continue!")
os.system('clear')

print("You walk outside. You are still in the capitol. The streets are empty, but you hear commotion in an alley. On you right lies the entrance to the alley. Straight in front of you lies the road. Both paths take you to your destination. Which way will you go?")
input("Press Enter to Continue!")
os.system('clear')

print("1) Right\n2) Straight ")
rl = input('')
while rl != '1' and rl != '2':
	rl = input("That isn't an option! Try again!")
input("Press Enter to continue!")
os.system('clear')

if rl == '1':
	print("You decide to go right, into the dark alley. As you walk, it gets darker, and the eerie bangs come from your sides. The deeper you walk, the louder the sounds become until finally a Wild Will stands before you!")
	input("Press Enter to Continue!")
	os.system('clear')

	'''#### ENEMY STATS ####'''

	enemyname = 'Wild Will'
	enemyhp=70
	enemystr=6
	enemyint=8
	enemyspd=18
	enemyhploss = 0
	enemyattackstring='The Wild Will ravages you with his trusty shiv dealing'
	enemyloot = "Propeller Hat"
	enemyexp = 60
	attack='0'
	playerhploss = 0

	'''#### ENEMY STATS ####'''

	fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
	inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

	print("The Wild Will crumbles to the floor. You push his corpse into the garbage on your left. In that pile, you notice some instructions for learning a new move!")
	input("Press Enter to Continue!")
	os.system('clear')

	print("You learned Cheap Shot!")
	newattackchoice2 = '1'

	print("The instructions read:'This attack will cripple your opponents, dealing 6 damage and halving their SPD stat!")
	input("Press Enter to continue!")
	os.system('clear')

	print("You exit the alley on the other side, thankful to have escaped that wretched place. The door to the security entrance of the throne room stands before you.")
	input("Press Enter to continue!")
	os.system('clear')



if rl == '2':
	print("You decide to go left, through the open street. As you walk people pass you on the sides. Suddenly, the Red Light District. A handsome man approaches you. 'Hey guys, I'm Magic Mike, do you have a minute to talk about Jesus?'")
	input("Press Enter to Continue!")
	os.system('clear')

	print("'No, sorry, we're very busy.' you say rather adamantly.'")
	input("Press Enter to Continue!")
	os.system('clear')

	print("'No, I insist.' says the magic man himself. You are going to need to fight your way out of this.")
	input("Press Enter to Continue!")
	os.system('clear')

	'''#### ENEMY STATS ####'''

	enemyname = 'Magic Mike'
	enemyhp=50
	enemystr=8
	enemyint=8
	enemyspd=20
	enemyhploss = 0
	enemyattackstring='Magic Mike reads scripture loudly, dealing'
	enemyloot = "Scantily Clad Wand"
	enemyexp = 50
	attack='0'
	playerhploss = 0

	'''#### ENEMY STATS ####'''

	fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
	inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

	print("Magic Mike submits and offers to teach you a new move!")
	input("Press Enter to continue!")
	os.system('clear')

	print("You learned Seduce!")
	newattackchoice2 = '2'

	print("Mike explains, 'Seduce halves your opponents STR and INT, making you take less damage from their attacks. It also deals 2 damage!'")
	input("Press Enter to continue!")
	os.system('clear')

	print("You make it to the end of the street in one piece, you see the security entrance to the throne room in front of you.")
	input("Press Enter to continue!")
	os.system('clear')


print("You go through the door, sneaking past the guards through the winding chambers. You slowly open the back door of the throne room. You see Connie drinking tea with her prized pet, the Z-nomorph: an alien creature discovered in a meteorite several years ago. It was delivered directly to the Queen herself upon its discovery, and it has stayed there ever since.")
input("Press Enter to continue!")
os.system('clear')

print("Connie seems to know you are coming for her. You now notice the power of your siblings radiating from her. You must find them first, slay them to stop her power from growing.")
input("Press Enter to continue!")
os.system('clear')

advisors = 3
print("Jack Fenton pokes your shoulder. 'Take this potion,' he says. 'It will make you stronger. You take the potion and all of your stats are severely increased. Turns out Jack Fenton became useful in the end.")
playerhpmax = playerhpmax * 2
playerstr = playerstr * 2
playerint = playerint * 2
playerspd += 10
hl = 1
jb = 1
sb = 1
os.system('clear')

print("You walk down the dusty hallways and find the offices of the Queen's loyal advisors. You know your siblings must be here somewhere. As you stroll down the hall, you find what you were looking for. The offices of Hungry Lockleer, Sea-Bastion, and John Bird stand before you.")

while advisors > 0 :
	print("Who Will you challenge first? \n1)Hungry Lockleer\n2)John Bird\n3)Sea-Bastion\nChoose Wisely")
	rl = input('')
	while rl != '1' and rl != '2' and rl != '3':
		rl = input("That isn't an option! Try again!")
	os.system('clear')

	if rl == '1' and hl != 0:
		print("You have chosen to challenge the mighty Henry Lockleer to a battle. You enter his office and see his true form. Had the Queen not drained so much of his energy, he would no doubt be the most powerful warrior in the kingdom. He turns to you with a face of recognition.")
		time.sleep(1)
		print("You are a traitor.")
		time.sleep(1)
		print("You abandoned the Queen.")
		time.sleep(1)
		print("HE MUST KILL YOU.")
		time.sleep(1.5)

		print("P r e s s   E n t e r   t o   c o n t i n u e.  .  .")
		input("")
		os.system('clear')

		'''#### ENEMY STATS ####'''

		enemyname = 'Henry Lockleer the Powerful'
		enemyhp=150
		enemystr=12
		enemyint=8
		enemyspd=26
		enemyhploss = 0
		enemyattackstring='Henry flexes his muscles, creating a powerful shockwave that knocks you over dealing'
		enemyloot = "Iron-Horned Helmet"
		enemyexp = 70
		attack='0'
		playerhploss = 0

		'''#### ENEMY STATS ####'''

		fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
		inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

		print("Henry Lockleer lets out his final sigh. He knows what you must do. You drain him of every last bit of energy he has. The Queen grows weaker.")
		advisors -= 1
		hl = 0

	elif rl == '2' and jb != 0:
		print("You have chosen to challenge the wise John Bird to a battle. You enter his office and see his true form. Had the Queen not drained so much of his energy, he would no doubt be the most intelligent man in the kingdom. He turns to you with a face of recognition.")
		time.sleep(1)
		print("You are a traitor.")
		time.sleep(1)
		print("You abandoned the Queen.")
		time.sleep(1)
		print("HE MUST KILL YOU.")
		time.sleep(1.5)

		print("P r e s s   E n t e r   t o   c o n t i n u e.  .  .")
		input("")
		os.system('clear')

		'''#### ENEMY STATS ####'''

		enemyname = 'John Bird the Wise'
		enemyhp=120
		enemystr=15
		enemyint=8
		enemyspd=32
		enemyhploss = 0
		enemyattackstring='John Bird enters your mind and floods you with vision of horrible avians dealing'
		enemyloot = "Chest-Mounted Mind Control Laser Raven"
		enemyexp = 70
		attack='0'
		playerhploss = 0

		'''#### ENEMY STATS ####'''

		fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
		inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

		print("John Bird lets out his final sigh. He knows what you must do. You drain him of every last bit of energy he has. The Queen grows weaker.")
		advisors -= 1
		jb = 0

	elif rl == '3' and sb != 0:
		print("You have chosen to challenge the quick Sea-Bastion to a battle. You enter his office and see his true form. Had the Queen not drained so much of his energy, he would no doubt be the most nimble man in the kingdom. He turns to you with a face of recognition.")
		time.sleep(1)
		print("You are a traitor.")
		time.sleep(1)
		print("You abandoned the Queen.")
		time.sleep(1)
		print("HE MUST KILL YOU.")
		time.sleep(1.5)

		print("P r e s s   E n t e r   t o   c o n t i n u e.  .  .")
		input("")
		os.system('clear')

		'''#### ENEMY STATS ####'''

		enemyname = 'Sea-Bastion the Quick'
		enemyhp=135
		enemystr=12
		enemyint=8
		enemyspd=65
		enemyhploss = 0
		enemyattackstring='Sea-Bastion dashes through you with extreme speed dealing'
		enemyloot = "Naruto's Shoes"
		enemyexp = 70
		attack='0'
		playerhploss = 0

		'''#### ENEMY STATS ####'''

		fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
		inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)
		print("Sea-Bastion lets out his final sigh. He knows what you must do. You drain him of every last bit of energy he has. The Queen grows weaker.")
		advisors -= 1
	else:
		print()

print("You have defeated all of the advisors, the Queen is at her weakest.")
input("Press Enter to continue!")
os.system('clear')

print("You make your way back to the throne room, but find the Z-nomorph waiting for you with the Queen nowhere to be found!")
input("Press Enter to continue!")
os.system('clear')

'''#### ENEMY STATS ####'''
	
enemyname = 'Z-nomorph'
enemyhp=165
enemystr=12
enemyint=8
enemyspd=40
enemyhploss = 0
enemyattackstring='The Z-nomorph lunges towards you and rakes you with his teeth dealing'
enemyloot = "Demi-God Staff"
enemyexp = 100
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

print("The Queen hears the painful cries of her fallen friend. She comes out of hiding to see her best friend in its dying moments.")
input("Press Enter to continue!")
os.system('clear')

print("'You did this!' she screams!")
input("Press Enter to continue!")
os.system('clear')

print("'You... I recognize you. Are you... ")
input("Press Enter to continue!")
os.system('clear')

print("'No! It can't be!' Connie yells, recognizing you.")
input("Press Enter to continue!")
os.system('clear')

print("'The King is dead! He is never coming back! Just leave me be, there is nothing here for you!' yells Connie in desperation.")
input("Press Enter to continue!")
os.system('clear')

print("You will not let her flee from her crimes so easily.")
input("Press Enter to continue!")
os.system('clear')

print("Right before you charge the Queen, the throne room shakes violently, part of the cieling collapses and lands beside you.")
input("Press Enter to continue!")
os.system('clear')

print("A blue entity slowly forms in the air between you and the Queen. The spirit falls to the ground, panting in exhaustion.")
input("Press Enter to continue!")
os.system('clear')

print("'My Queen,' he says, 'I'm sorry. I have wronged you. Please forgive me. I will help you.'")
input("Press Enter to continue!")
os.system('clear')

print("Suddenly, the spirit vaporizes and flows directly into the Queen. The King and Queen have had their spirits melded and the Queen appears stronger than ever. Rather than relying on the King's children for her power, the Queen has now absorbed the King's full strength.")
input("Press Enter to continue!")
os.system('clear')

print("Jack Fenton cowers behind a pillar in fear. The Queen falls to her knees, overwhelmed by her new power. She starts to adapt to her newfound power, creating bursts of energy on her sides and destroying the rubble between you and her.")
input("Press Enter to continue!")
os.system('clear')

print("The Queen Attacks!")
input("Press Enter to continue!")
os.system('clear')

'''#### ENEMY STATS ####'''
	
enemyname = ''
enemyhp= 200
enemystr=14
enemyint=8
enemyspd=70
enemyhploss = 0
enemyattackstring='The Queen strikes you with the full extent of her overwhelming power dealing'
enemyloot = "Spirit-Infused God Staff"
enemyexp = 100
attack='0'
playerhploss = 0

'''#### ENEMY STATS ####'''

fightstart(enemyhp,enemyname,playername,attack, enemyhploss, playerhploss, playerhpmax, playerinv, enemyint, enemystr, enemyspd, enemyattackstring, enemyloot, enemyexp, playerstrcurrent, playerintcurrent, playerspdcurrent)
inventory(item, totalitems, playerinv, equippeditems,invchoice, equip, examine)

print("It is done. The Queen is dead and the King's spirit is forever vanquished. You alone stand as the heir to the throne. You open the doors on the far end of the throne room and walk onto the balcony that overlooks the kingdom. You did it. All you can see is yours. The people, hearing the commotion from the throne room, have already gathered outside. They are thrilled to see their cruel Queen defeated, and happy to see a new, kinder face on the throne.")

















