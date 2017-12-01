print("Welcome to the Friend Simulator! What do you want to talk about?\n")
conversation=''
while conversation != 'Goodbye':
	conversation=str(input("Sports, Politics, Video-Games, School, or Deep-Seeded-Emotional-Issues, or Goodbye \n"))
	if conversation=='Sports':
		print("Man that team sure is scoring points sometimes. Sometimes they don't score points and that upsets me. \n")
	elif conversation=='Politics':
		print("Man that politician sure is doing good things. Other politics do bad things also thanks.\n")
	elif conversation=='Video-Games':
		print("Gamestop is still socially relevant, I'm sure of it.\n")
	elif conversation=='Deep-Seeded-Emotional-Issues':
		print("Please ask me something else, I don't want to talk about it\n")
	elif conversation=='School':
		print("If I don't get into college I'm going to buy a gun and trade it for a bear out west. \n")
