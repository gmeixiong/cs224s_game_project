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
	    firstAttackQueries = ["Please input a coordinate for attack!", "Where do you want to attack first?", "Initial target coordinates, captain?"]
	    attackQueries = ["Please input a coordinate for attack!", "Next attack coordinates, captain?", "Where do you want to attack next?", "Where should we fire next?"]
	    losingStarts = ["We're not out of this yet, Captain!", "It ain't over 'til it's over!", "Time for a comeback!"]
	    winningStarts = ["We've got them on the ropes!", "Victory is on the horizon, Captain!", "We've got them right where we want them."]
	    hitStarts = ["Let's get 'em again, Captain", "Once more, with feeling!", "Another!"]
	    missStarts = ["This time, for sure!", "Give it another go, Captain!", "A little more thataways, Captain!"]
	    twiceHitStarts = ["For Fire!!"]
	    twiceMissStarts = ["Third times the charm!"]

	      #Location Status
	    haveFiredResponses = ["Yes! You've already fired at this location!", "Affirmative, Captain", "Aye, Captain, we've shot there."]
	    haveNotFiredResponses = ["Nope! You haven't fired here yet!", "Not yet Captain", "Nope, haven't pointed the cannon there, sir!"]
	    haveShipResponses = ["Yep, we've got one there.", "Yessir, got one of our best guys out there!"]
	    haveNotShipsResponses = ["Nope! You don't have a ship here", "That's a negative Ghost Rider"]

	      #Already Seen
	    seenResponses = ["You've already fired here, Captain. Choose somewhere else.", "Can only do that once, Captain. Try again.", "Lightning doesn't strike in the same place twice, Captain. Try something else."]



	    if state.prevResult == None:
	      	userInput = raw_input(random.choice(firstAttackQueries))
	    else:
	      	query = random.choice(attackQueries)
	      	roll = random.randint(1, 10)
	      	if len(state.playerShips) <= 3 and roll >= 3:
	      		query = random.choice(losingStarts) + " " + query
	      	elif len(state.cpuShips) <= 3 and roll >= 3:
	      		query = random.choice(winningStarts) + " " + query
	      	elif state.doubleMiss and roll >= 5:
	      		query = random.choice(twiceMissStarts) + " " + query
	      	elif state.doubleHit and roll >= 5:
	      		query = random.choice(twiceHitStarts) + " " + query
	      	elif state.prevResult == "hit" and roll >= 2:
	      		query = random.choice(hitStarts) + " " + query
	      	elif state.prevResult == "miss" and roll >= 2:
	      		query = random.choice(missStarts) + " " + query
	      	userInput = raw_input(query)
	    userInput = userInput.lower()


	    coordinates = get_coord(userInput) # parse coordinates will fill the coordinates list with the list of parsed coordinates. Returns 1 if 1 successful coordinate. returns 2 if more than one coordinate. Returns 0 otherwise.
	    status = len(coordinates)
	    if status >= 2:
	    	status = 2
	    if status == 1 or referencedCoordinate is not None and len(re.findall("(?:.*)(fire|shoot|attack|go)(?:.*)", userInput)) > 0:
	      	#coordinates were parsed. firing at input target. add target to list. return whether target was hit or miss.
	      	if len(re.findall("(?:.*)(have|did)(?:.*)", userInput)) > 0:
	      		if len(re.findall("(?:.*)(fire|target|shot|done|attack)(?:.*)", userInput)) > 0:
	      			if coordinates[0] in state.targeted:
	      				print(random.choice(haveFiredResponses))
	      			else:
	      				print(random.choice(haveNotFiredResponses))
	      				referencedCoordinate = coordinates[0]
	      		####################Should be option to fire at this target here #####################
	      		elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
	      			if coordinates[0] in state.playerShips:
	      				print(random.choice(haveShipResponses))
	      			else:
	      				print(random.choice(haveNotShipsResponses))
	      		else:
	      			print("I'm not sure what you mean! Please try again")
	      	else:
	      		print("Firing...")
	      		if len(coordinates) == 0 and referencedCoordinate is not None:
	      			coordinates.append(referencedCoordinate)
	      		#state.targeted.append(coordinates[0]) ##
	      		## APPEND THIS COORDINATE TO TARGETEDPOInts LIST
	      		if state.guessed(coordinates[0]):#already guessed
	      			print random.choice(seenResponses)
	      			return parseFireInput(state)#just start the whole process over
		      	return coordinates[0]

	    elif status == 2: #coordinates has more than 1
	      	if len(re.findall("(?:.*)(have|previous|last|past|did)(?:.*)", userInput)) > 0:
	      		if len(re.findall("(?:.*)(fire|target|shot|done|gone|attack|shoot)(?:.*)", userInput)) > 0:
	      			if len(state.targeted) > 0:
		      			print("You have already targeted the following coordinates: ")
		      			targets = list(state.targeted)
		      			for i in range(len(targets)):
		      				print("Row: %d, Column: %d\n") % (targets[i][0], targets[i][1])
		      		else:
		      			print("You have not fired at any points yet.")
		      	elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
	      			print("You're ships are stationed at the following coordinates: ")
	      			ships = list(state.playerShips)
	      			for i in range(len(ships)):
						print("Row: %d, Column: %d\n") % (ships[i][0], ships[i][1])
						#self.coordinates is list of user's ships coordinates. each coordinate entry is a 2 element array where [0] is row and [1] is column
	  		else:
	  			response = multipleTargetsResponses[random.randint(0, len(multipleTargetsResponses)) - 1]
	      		print response

	    elif len(re.findall("(?:.*)(have|previous|last|past|did)(?:.*)", userInput)) > 0:
	      	if len(re.findall("(?:.*)(hit|destroy|land)(?:.*)", userInput)) > 0:
		      	print("You have hit ships at the following coordinates: ")
		      	hits = list(state.hit)
		      	for i in range(len(hits)):
		      		print("Row: %d, Column: %d\n") % (hits[i][0], hits[i][1])

      		elif len(re.findall("(?:.*)(fire|target|shot|done|gone|attack|shoot)(?:.*)", userInput)) > 0:
      			if len(state.targeted) > 0:
	      			print("You have already targeted the following coordinates: ")
	      			targets = list(state.targeted)
	      			for i in range(len(targets)):
	      				print("Row: %d, Column: %d\n") % (targets[i][0], targets[i][1])
	      		else:
	      			print("You have not fired at any points yet.")

	      	elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
      			print("You're ships are stationed at the following coordinates: ")
      			ships = list(state.playerShips)
      			for i in range(len(ships)):
					print("Row: %d, Column: %d\n") % (ships[i][0], ships[i][1])
					#self.coordinates is list of user's ships coordinates. each coordinate entry is a 2 element array where [0] is row and [1] is column

		elif len(re.findall("(?:.*)(my)(?:.*)", userInput)) > 0:
			print("You're ships are stationed at the following coordinates: ")
			ships = list(state.playerShips)
			for i in range(len(ships)):
				print("Row: %d, Column: %d\n") % (ships[i][0], ships[i][1])
				#self.coordinates is list of user's ships coordinates. each coordinate entry is a 2 element array where [0] is row and [1] is column

	    else:
	      	print("Sorry, I didn't quite catch that. Can you try again??")