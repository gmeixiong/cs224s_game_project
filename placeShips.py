import re
import string
import random
import numpy as math
from coord import *

def aligned(coordinates):
    if coordinates[0] == coordinates[1] or coordinates[0] == coordinates[2] or coordinates[1] == coordinates[2]:
        return False
    if coordinates[0][0] == coordinates[1][0] and coordinates[1][0] == coordinates[2][0]:
		coordinates = sorted(coordinates, key = lambda x: x[1])
		if coordinates[0][1] + 1 == coordinates[1][1] and coordinates[1][1] + 1 == coordinates[2][1]:
			return True
    elif coordinates[0][1] == coordinates[1][1] and coordinates[1][1] == coordinates[2][1]:
		coordinates = sorted(coordinates, key = lambda x: x[0])
		if coordinates[0][0] + 1 == coordinates[1][0] and coordinates[1][0] + 1 == coordinates[2][0]:
			return True
    else:
    	return False

def get_other_coord(state, coordinates):
	first_coord = coordinates[0]
	second_coord = coordinates[1]

	poss_coords = []

	if first_coord[0] == second_coord[0]:
		diff = math.abs(first_coord[1] - second_coord[1])
		if diff == 0:
			print 'ERROR, same coordinates'
		elif diff == 1:
			if second_coord[1] > first_coord[1]:
				if state.checkValid([first_coord[0], second_coord[1]+1]):
					poss_coords.append([first_coord[0], second_coord[1]+1])
				if state.checkValid([first_coord[0], first_coord[1]-1]):
					poss_coords.append([first_coord[0], first_coord[1]-1])
			else:
				if state.checkValid([first_coord[0], first_coord[1]+1]):
					poss_coords.append([first_coord[0], first_coord[1]+1])
				if state.checkValid([first_coord[0], second_coord[1]-1]):
					poss_coords.append([first_coord[0], second_coord[1]-1])
		elif diff == 2:
			if second_coord[1] > first_coord[1]:
				if state.checkValid([first_coord[0], first_coord[1]+1]):
					poss_coords.append([first_coord[0], first_coord[1]+1])
			else:
				if state.checkValid([first_coord[0], first_coord[1]-1]):
					poss_coords.append([first_coord[0], first_coord[1]-1])
		else: 
			print 'ERROR, coordinates don\'t align'

	elif first_coord[1] == second_coord[1]:
		diff = math.abs(first_coord[0] - second_coord[0])
		if diff == 0:
			print 'ERROR, same coordinates'
		elif diff == 1:
			if second_coord[0] > first_coord[0]:
				if state.checkValid([first_coord[0]-1, second_coord[1]]):
					poss_coords.append([first_coord[0]-1, second_coord[1]])
				if state.checkValid([second_coord[0]+1, first_coord[1]]):
					poss_coords.append([second_coord[0]+1, first_coord[1]])
			elif second_coord[0] < first_coord[0]:
				if state.checkValid([first_coord[0]+1, second_coord[1]]):
					poss_coords.append([first_coord[0]+1, second_coord[1]])
				if state.checkValid([second_coord[0]-1, first_coord[1]]):
					poss_coords.append([second_coord[0]-1, first_coord[1]])
		elif diff == 2:
			if second_coord[0] > first_coord[0]:
				if state.checkValid([first_coord[0]+1, first_coord[1]]):
					poss_coords.append([first_coord[0]+1, first_coord[1]])
			else:
				if state.checkValid([first_coord[0]-1, first_coord[1]]):
					poss_coords.append([first_coord[0]-1, first_coord[1]])
		else: 
			print 'ERROR, coordinates don\'t align'
	else:
		print 'THESE COORDINATES DON\'T ALIGN'
	return poss_coords

def coordStr(c):
	rows=['0','a','b','c','d','e']
	return rows[c[0]]+str(c[1])

def getOverlap(state, coordinates):
	overlap = []
	for c in coordinates:
		if not state.checkFree(c):
			overlap.append(c)

def which_coord(c1, c2, response):
	# sc1 = str(c1)[1:-1]
	# sc2 = str(c2)[1:-1]
	sc1 = coordStr(c1)
	sc2 = coordStr(c2)
	if 'first' in response or sc1 in response or sc1.replace(" ", "") in response or sc1.replace(",", "") in response:
		return c1
	elif 'second' in response or sc2 in response or sc2.replace(" ", "") in response or sc2.replace(",", "") in response:
		return c2
	else:
		return [-1,-1]

def universalPrompt(userInput, state):
	userInput = userInput.lower()
	if "help" in userInput:
		print "Possible Actions:"
		print "1) Input coordinates to place ships i.e. a4, 4a, 1,3, row 1 col 3"
		print "2) Ask where your ships are i.e. \"Where did I placed my ships?\""
		print "3) Ask where you've fired i.e. \"Where have I fired?\""
		print "4) Ask which ships you've sunk i.e. \"Which ships have I sunk\""
	elif "start over" in userInput or "startover" in userInput or "restart" in userInput:
	    print "Starting over"
	    state.restart()

def parseShipPlacement(state):
	userInput = raw_input("Where would you like to place your ship?")
	# responseForOne = {0: "That's a great start! Now I just need two more coordinates to place your ship", 
	# 1: "Ok great!", 2: ""}
	universalPrompt(userInput, state)

	askForShipQueries = ["Where would you like to place your ship?", "Where do you want your ship to be?", "Captain, where should I anchor this vessel?"]
	noCoordinateResponses = ["Sorry. I didn't catch any coordinates in your response.", "I didn't catch where you said, Captain."]
	genericPraise = ["Great!", "Perfect!", "Lovely!", "Awesome!", "Excellent!"]
	tryPlaceResponses = ["I'll see if I can place your ship at coordinates: ", "I'll try placing your ship at coordinates: ", "I'll go check on the feasability of coordinates: "]
	tooManyShipsResponses = ["Uhh Captain? We don't have ships that long.", "That's too many, Captain. Our ships can only cover three.", "Three be the magic number. Four is too many, and Five is right out!", "Sorry, you're providing too many coordinates."]
	didntUnderstandResponses = ["Sorry, I didn't get that.", "Sorry I didn't understand that.", "Come again, Captain?"]

	coordinates = []
	while len(coordinates) < 3:
		userInput = userInput.lower()
		coord = get_coord(userInput)
		if len(re.findall("(?:.*)(have|did|where)(?:.*)", userInput)) > 0:
			if len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
				if len(state.playerShips) == 0:
					print("You have not placed any ships yet!")
				else:
					print("You have placed ships at the following coordinates: ")
					ships = list(state.playerShips)
					print state.playerShips
	      			for i in range(len(ships)):
						print("Row: %d, Column: %d\n") % (ships[i][0], ships[i][1])
        		else:
      			        print("I'm not sure what you mean! Please try again")

		if len(coord) == 0:
			userInput = raw_input(random.choice(noCoordinateResponses) +  " " + random.choice(askForShipQueries))
			universalPrompt(userInput, state)

		elif len(coord) == 1:
			co = coord[0]
			# if not state.checkFree(co):
					# userInput = raw_input("There's already a ship at that spot. Where else would you like to place your ship?")
			if len(coordinates) == 0:
				# if not state.neighborsFree(co):
					# userInput = raw_input("You wouldn't be able to place a whole ship that includes that coordinate. Where else would you like to place your ship?")
				# else:
				userInput = raw_input("That's a great start! Now just tell me two more coordinates to place your ship")
				universalPrompt(userInput, state)
				coordinates.append(co)

			elif len(coordinates) == 1:
				dum_co = coordinates
				dum_co.append(co)
				poss_coords = get_other_coord(state, dum_co)
				if len(poss_coords) == 0:
					userInput = raw_input("Sorry, that coordinate doesn't align with your first coordinate " + coordStr(co) + " . Please tell me two more coordinates that align with this coordinate")
					universalPrompt(userInput, state)
				else:
					# coordinates.append(co)
					if len(poss_coords) == 1:
						# if not state.checkFree(poss_coords[0]):
							# userInput = raw_input("Sorry, this ship would overlap with another ship. Let's try again. Where would you like to place your ship?")
							# continue
						# else:
						userInput = raw_input(random.choice(genericPraise) + " So the last coordinate will be " + coordStr(poss_coords[0]) + ", correct?")
						universalPrompt(userInput, state)
						
						if 'n' in userInput.lower() or 'change' in userInput.lower():
							userInput = raw_input("Do you want to place your ship at a different location?")
							universalPrompt(userInput, state)
							if 'n' in userInput.lower():
								print 'Ok so the last coordinate will have to be ' + coordStr(poss_coords[0]) + '. I will place your ship now!'
								coordinates.append(poss_coords[0])
							elif 'y' in userInput.lower():
								coordinates = []
								userInput = raw_input(random.choice(genericPraise) + " " + random.choice(askForShipQueries))
								universalPrompt(userInput, state)
							else:	
								coordinates = []
								userInput = raw_input(random.choice(didntUnderstandResponses) + " Let's try again. Where would you like to place your ship?")
								universalPrompt(userInput, state)
						else:
							coordinates.append(poss_coords[0])
							resp = random.choice(tryPlaceResponses)
							for c in coordinates:
								resp = resp + " " + coordStr(c)
							print resp
							print str(coordinates)

					else:
						userInput = raw_input(random.choice(genericPraise) + " So for your last coordinate, do you want to make it "+ coordStr(poss_coords[0]) + " or " + coordStr(poss_coords[1]) + 
						"?")
						universalPrompt(userInput, state)
						last_coord = which_coord(poss_coords[0], poss_coords[1], userInput.lower())
						while last_coord[0] < 0:
							userInput = raw_input(random.choice(didntUnderstandResponses) + " For your last coordinate, do you want to make it "+ coordStr(poss_coords[0]) + " or " + coordStr(poss_coords[1]) + 
						"?")
							universalPrompt(userInput, state)
							last_coord = which_coord(poss_coords[0], poss_coords[1], userInput.lower())
						print random.choice(genericPraise) +  " So your last coordinate is " + coordStr(last_coord) + ". " + random.choice(tryPlaceResponses)
						coordinates.append(last_coord)
						##ADD AFFIRMING AND GETTING LAST COORDINATE, AFTER FINDING MISSING COORDINATE
						

			elif len(coordinates)==2: 
				dum_co = coordinates
				dum_co.append(co)
				if state.aligned(dum_co):
					coordinates.append(co)
					resp = random.choice(genericPraise) + random.choice(tryPlaceResponses)
					for c in coordinates:
						resp = resp + " " + coordStr(c)
					print resp
				else:
					userInput = raw_input("Sorry, that last coordinate doesn't align with the other two coordinates you picked. Please tell me one last coordinate that aligns with your previous selected ones")

		elif len(coord) == 2:
			if len(coordinates) > 1:
				userInput = raw_input(random.choice(tooManyShipsResponses) + " What's the last coordinate you'd like this ship to cover?")
				universalPrompt(userInput, state)
			elif len(coordinates) == 1:
				dum_co = coordinates
				dum_co.extend(coord)
				if state.aligned(dum_co):
					coordinates.extend(coord)
					resp = random.choice(tryPlaceResponses)
					for c in coordinates:
						resp = resp + " " + coordStr(c)
					print resp
					# print "Great! I'll place your ship at coordinates: " + str(coordinates)
				else:
					userInput = raw_input("Sorry, those coordinates don't align with your first coordinate " + coordStr(coordinates[0]) + " . Please tell me two more coordinates that align with this coordinate")
					universalPrompt(userInput, state)
			elif len(coordinates) == 0:
				poss_coords = get_other_coord(state, coord)
				if len(poss_coords) == 0:
					userInput = raw_input("Sorry, those coordinates don't align. At which coordinates would you like to place your ship?")
					universalPrompt(userInput, state)
				else:
					coordinates.extend(coord)
					if len(poss_coords) == 1:
						userInput = raw_input(random.choice(genericPraise) + " So the last coordinate will be " + coordStr(poss_coords[0]) + ", correct?")
						universalPrompt(userInput, state)
						if 'n' in userInput.lower() or 'change' in userInput.lower():
							userInput = raw_input("Do you want to place your ship at a different location?")
							universalPrompt(userInput, state)
							if 'n' in userInput.lower():
								print 'Ok so the last coordinate will have to be ' + coordStr(poss_coords[0]) + '. Let me see if I can place your ship here!'
								coordinates.append(poss_coords[0])
							elif 'y' in userInput.lower():
								coordinates = []
								userInput = raw_input("Cool, so where would you like to place your ship?")
								universalPrompt(userInput, state)
							else:	
								coordinates = []
								userInput = raw_input(random.choice(didntUnderstandResponses) + " Let's try again. Where would you like to place your ship?")
								universalPrompt(userInput, state)
						else:
							coordinates.append(poss_coords[0])
							resp = random.choice(tryPlaceResponses)
							for c in coordinates:
								resp = resp + " " + coordStr(c)
							print resp

					else:
						userInput = raw_input("Great, so for your last coordinate, do you want to make it "+ coordStr(poss_coords[0]) + " or " + coordStr(poss_coords[1]) + 
						"?")
						universalPrompt(userInput, state)
						last_coord = which_coord(poss_coords[0], poss_coords[1], userInput.lower())
						while last_coord[0] < 0:
							userInput = raw_input(random.choice(didntUnderstandResponses) + " For your last coordinate, do you want to make it "+ str(poss_coords[0]) + " or " + str(poss_coords[1]) + 
						"?")
							universalPrompt(userInput, state)
							last_coord = which_coord(poss_coords[0], poss_coords[1], userInput.lower())
						print random.choice(genericPraise) + " I'll make your last coordinate " + coordStr(last_coord) + ". I'll see if I can place your ship now!"
						coordinates.append(last_coord)
						##ADD AFFIRMING AND GETTING LAST COORDINATE, AFTER FINDING MISSING COORDINATE

		elif len(coord) == 3:
			if len(coordinates) != 0:
				resp = random.choice(tooManyShipsResponses) + " So far, your ship covers"
				for c in coordinates:
					resp = resp + " " + coordStr(c)
				userInput = raw_input(resp + ". Which other coordinates do you want this ship to cover? ")
				universalPrompt(userInput, state)
			else:
				if state.aligned(coord):
					coordinates.extend(coord)
					resp = random.choice(tryPlaceResponses)
					for c in coordinates:
						resp = resp + " " + coordStr(c)
					print resp
					# print "Great! I'll place your ship at coordinates: " + str(coordinates)
				else:
					userInput = raw_input("Sorry, these coordinates don't line up together. Which coordinates would you like your ship to cover?")
		else:
			resp = random.choice(tooManyShipsResponses) + " So far, your ship covers"
			if len(coordinates) == 0: 
				resp += " no coordinates"
			else:
				for c in coordinates:
					resp = resp + " " + coordStr(c)
			userInput = raw_input(resp + ". Which other coordinates do you want this ship to cover? ")
			universalPrompt(userInput, state)


	return coordinates

		# if 'y' in userInput.lower():
		# 		userInput = raw_input("Ok great! I'll make this the center of the ship. Now do you want your ship to be oriented horizontally or vertically?")
		# 		if 'h' in userInput.lower():
		# 			print 'Ok! I\'ll place your ship horizontally centered around ' + str(coord)
		# 		elif 'v' in userInput.lower():
		# 			print 'Ok! I\'ll place your ship vertically centered around ' + str(coord)

		# 	elif 'n' in userInput.lower():
		# 		userInput = raw_input("Ok. Where do you want to ")

		# 	else:


		# elif len(coord) == 2:
		# 	poss_coords = get_other_coord(coord)
		# 	userInput = raw_input("Which coordinate do you want to complete your ship placement? Choose out of " + str(poss_coords))

		# elif len(coord) == 3:
		# 	if aligned(coord):
		# 		print "Great! I'll place your ship at coordinates: " + str(coord)
		# 	else:
		# 		print "Those coordinates don\'t align, please enter them again!"
		# 	userInput = raw_input("Ya wanna put your ships here in these coordinates: " + str(coord))
		# else:
		# 	print 'too many coordinates!! not enought time'


	# while True:
	# 	userInput = userInput.lower()
	# 	# print userInput
	# 	coord = get_coord(userInput)

		# if len(coord) == 0:
		# 	userInput = raw_input("Sorry. I didn't catch any coordinates in your response. Where would you like to place your ships?")
		# 	continue

		# elif len(coord) == 1:
		# 	userInput = raw_input("Do you want this coordinate to be the center of the ship?")
		# 	if 'y' in userInput.lower():
		# 		userInput = raw_input("Ok great! I'll make this the center of the ship. Now do you want your ship to be oriented horizontally or vertically?")
		# 		if 'h' in userInput.lower():
		# 			print 'Ok! I\'ll place your ship horizontally centered around ' + str(coord)
		# 		elif 'v' in userInput.lower():
		# 			print 'Ok! I\'ll place your ship vertically centered around ' + str(coord)

		# 	elif 'n' in userInput.lower():
		# 		userInput = raw_input("Ok. Where do you want to ")

		# 	else:


		# elif len(coord) == 2:
		# 	poss_coords = get_other_coord(coord)
		# 	userInput = raw_input("Which coordinate do you want to complete your ship placement? Choose out of " + str(poss_coords))

		# elif len(coord) == 3:
		# 	if aligned(coord):
		# 		print "Great! I'll place your ship at coordinates: " + str(coord)
		# 	else:
		# 		print "Those coordinates don\'t align, please enter them again!"
		# 	userInput = raw_input("Ya wanna put your ships here in these coordinates: " + str(coord))
		# else:
		# 	print 'too many coordinates!! not enought time'

		# print coord

# state = 0
# c= parseShipPlacement(state)
# print c
