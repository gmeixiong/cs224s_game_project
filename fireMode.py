#firing 
# ask for coordinates for where to fire
# ask about past attempts at firing
# ask ask about my coordinates for ships
import re
import string
import random
from coord import *

##CHANGE ALL SELF.VARS TO STATE.VAR

# state.targeted = [] # list of all points that user has already targeted
# state.hit = [] #list of all points that user has already hit (targeted points which were successful)
# state.playerShips = [] #list of coordinates of user's ships. Each element of this list is a two-element list which represents row (0th element) x column (1st element)

def parseFireInput(state):
	referencedCoordinate = None
	multipleTargetsResponses = ['Hey!! You can\'t fire at more than one place! Please try again!', 'No shooting at multiple places! Put in one coordinate!', 'Your Battleship is only equipped with one bullet per round! Please input one coordinate!',
'Not enough ammo! Only enough for one coordinate!']
	while True:
	      #targetGrid is a battleship grid with the opponent's ships. Thinking about numpy array
	      #from parseCoordinates, returns 0 if parse fail and 1 if parse success, 2 if parse returns multiple coordinats. coordinates will return with the 0th element as the row and 1st element as the column

	      # First Screen and Input
	      userInput = raw_input("Please input a coordinate for attack!")
	      userInput = userInput.lower()

	      coordinates = []

	      coordinates = get_coord(userInput) # parse coordinates will fill the coordinates list with the list of parsed coordinates. Returns 1 if 1 successful coordinate. returns 2 if more than one coordinate. Returns 0 otherwise.
	      status = len(coordinates)
	      if status >= 2:
	      	status = 2
	      if status == 1 or self.referencedCoordinate is not None and len(re.findall("(?:.*)(fire|shoot)(?:.*)", userInput)) > 0:
	      	#coordinates were parsed. firing at input target. add target to list. return whether target was hit or miss.
	      	if len(re.findall("(?:.*)(have)(?:.*)")) > 0:
	      		if len(re.findall("(?:.*)(fire|target|shot|done)(?:.*)", userInput)) > 0:
	      			if coordinates[0] in state.targeted:
	      				print("Yes! You've already fired at this location!")
	      			else:
	      				print("Nope! You haven't fired here yet!")
	      				referencedCoordinate = coordinates[0]
	      		elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
	      			if coordinates[0] in state.playerShips:
	      				print("Yes! You have a ship at this location.")
	      			else:
	      				print("Nope! You don't have a ship here")
	      		else:
	      			print("I'm not sure what you mean! Please try again")
	      	else:
	      		print("Firing...")
	      		if len(coordinates) == 0 and referencedCoordinate is not None:
	      			coordinates.append(referencedCoordinate)
	      		#state.targeted.append(coordinates[0]) ##
	      		## APPEND THIS COORDINATE TO TARGETEDPOInts LIST
		      	return coordinates[0]

	      elif status == 2: #coordinates has more than 1
	      	if len(re.findall("(?:.*)(have)(?:.*)")) > 0:
	      		if len(re.findall("(?:.*)(fire|target|shot|done)(?:.*)", userInput)) > 0:
	      			if len(state.targeted) > 0:
		      			print("You have already targeted the following coordinates: ")
		      			for i in range(len(state.targeted)):
		      				print("Row: %d, Column: %d\n") % (state.targeted[i][0], state.targeted[i][1])
		      		else:
		      			print("You have not fired at any points yet.")
		      	elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
	      			print("You're ships are stationed at the following coordinates: ")
	      			for i in range(len(state.playerShips)):
	  					print("Row: %d, Column: %d\n") % (state.playerShips[i][0], state.playerShips[i][1])
	  		else:
	  			response = multipleTargetsResponses[random.randint(0, len(multipleTargetsResponses)) - 1]
	      		print response
	      elif len(re.findall("(?:.*)(last|past|previous|fire|gone|shoot|shot)(?:.*)", userInput)) > 0:
	      	print("You have already targeted the following coordinates: ")
	      	for i in range(len(state.targeted)):
	      		print("Row: %d, Column: %d\n") % (state.targeted[i][0], state.targeted[i][1])

	      elif len(re.findall("(?:.*)(hit)(?:.*)", userInput)) > 0:
	      	print("You have sunk ships at the following coordinates: ")
	      	for i in range(len(state.hit)):
	      		print("Row: %d, Column: %d\n") % (state.hit[i][0], state.hit[i][1])

	      elif len(re.findall("(?:.*)(my)(?:.*)", userInput)) > 0:
	      	print("You're ships are stationed at the following coordinates: ")
	      	for i in range(len(state.playerShips)):
	      		print("Row: %d, Column: %d\n") % (self.myShips[i][0], self.myShips[i][1])
	      		#self.coordinates is list of user's ships coordinates. each coordinate entry is a 2 element array where [0] is row and [1] is column

	      else:
	      	print("Sorry, I didn't quite catch that. Can you try again??")