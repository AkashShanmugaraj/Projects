import random
innings_count = 0
#there are 10 possible actions - 0,1,2,3,4,5,6,7,8,9
#therefor the value generated by the computer is given by
computerplay = random.randint(0,9)

userscore = 0
computerscore = 0


#Batting and Bowling Functions
def play_bat():
	global innings_count, computerplay, userplay, userscore, computerscore
	innings_count+=1
	print("You are now batting")
	userplay = 0
	while computerplay != userplay: 
		print("Enter your decision")
		userplay = int(input(""))
		if userplay not in range(0,10):
			print("Only values from 0 to 9 are allowed")
			play_bat()
		computerplay = random.randint(0,9)
		print("Computer's Decision is", computerplay)
		
		if computerplay != userplay: 
			userscore += userplay
			print(userscore)

	if computerplay == userplay:
		print("You are OUT!")
		if innings_count == 2:
			print("Game Over")
			final = userscore-computerscore
			if userscore > computerscore:
				print("You Win by", final)
			elif computerscore > userscore:
				print("The computer won by", abs(final))
		elif innings_count == 1:
			print("The Computer will be batting next")
			play_bowl()

def play_bowl():
	global innings_count, computerplay, userplay, userscore, computerscore
	innings_count+=1
	print("You are now bowling")
	userplay = 0
	while computerplay != userplay: 
		print("Enter your decision")
		userplay = int(input(""))
		if userplay not in range(0,10):
			print("Only values from 0 to 9 are allowed")
			play_bowl()
		computerplay = random.randint(0,9)
		print("Computer's Decision is", computerplay)
		
		if computerplay != userplay: 
			computerscore += computerplay
			print(computerscore)

	if computerplay == userplay:
		print("The Computer is OUT!")
		if innings_count == 2:
			print("Game Over")
			final = userscore-computerscore
			if userscore > computerscore:
				print("You Win by", final)
			elif computerscore > userscore:
				print("The computer won by", abs(final))
		elif innings_count == 1:
			print("You will be batting next")
			play_bat()

#For the toss, sum of the values of computerplay and userplay must be even or odd
print("Time for toss. Input 1 for Odd and 2 for Even")
usertoss = int(input(""))
computerplay = random.randint(0,9)
print("Computer's Decision is")
print(computerplay)
toss = usertoss+computerplay
if toss%2 == 0:
	outvalue = 2
elif toss%2 == 1:
	outvalue = 1
decision = ""
if usertoss == outvalue:
	print("You have won the toss")
	print("Input 1 to choose batting and 2 to input Bowling")
	batorbowl = int(input(""))
	if batorbowl == 1:
		decision = "Bat"
		play_bat()
	elif batorbowl == 2:
		decision = "Bowl"
		play_bowl()

elif usertoss != outvalue:
	batorbowl = random.randint(1,2)
	print("You lost the toss")
	if batorbowl == 1:
		print("The computer chose Batting and hence you will be bowling")
		decision = "Bowl"
		play_bowl()
	elif batorbowl == 2:
		print("The computer chose Bowling and hence you will be batting")
		decision = "Bat"
		play_bat()

