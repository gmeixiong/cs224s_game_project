#firing 
# ask for coordinates for where to fire
# ask about past attempts at firing
# ask ask about my coordinates for ships
import re
import string
import random
from coord.py import *

loop = 3
while loop == 3:
      print("---------------------------------------------------------")
      print("Welcome to Battleships")
      print("Note: please type all our reponses in quotes.")
      print("---------------------------------------------------------")


      multipleTargetsResponses = ['Hey!! You can\'t fire at more than one place! Please try again!', 'No shooting at multiple places! Put in one coordinate!', 'Your Battleship is only equipped with one bullet per round! Please input one coordinate!',
      'Not enough ammo! Only enough for one coordinate!']

      #targetGrid is a battleship grid with the opponent's ships. Thinking about numpy array
      #from parseCoordinates, returns 0 if parse fail and 1 if parse success, 2 if parse returns multiple coordinats. coordinates will return with the 0th element as the row and 1st element as the column

      # First Screen and Input
      userInput = input("Where would you like to fire? ")
      targetedPoints = []
      hitPoints = []
      coordinates = []
      myShips = []
      userInput = userInput.lower()
      referencedCoordinate = None
      status = parseCoordinates(userInput, coordinates)
      if status == 1 or referencedCoordinate is not None and len(re.findall("(?:.*)(fire|shoot)(?:.*)", userInput)) > 0:
      	#coordinates were parsed. firing at input target. add target to list. return whether target was hit or miss.
      	if len(re.findall("(?:.*)(have)(?:.*)")) > 0:
      		if len(re.findall("(?:.*)(fire|target|shot|done)(?:.*)", userInput)) > 0:
      			if coordinates[0] in targetedPoints:
      				print("Yes! You've already fired at this location!")
      			else:
      				print("Nope! You haven't fired here yet!")
      				referencedCoordinate = coordinates[0]
      		elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
      			if coordinates[0] in myShips:
      				print("Yes! You have a ship at this location.")
      			else:
      				print("Nope! You don't have a ship here")
      		else:
      			print("I'm not sure what you mean! Please try again")
      	else:
      		print("Firing...")
      		if len(coordinates) == 0 and referencedCoordinate is not None:
      			coordinates.append(referencedCoordinate)
      		targetedPoints.append(coordinates[0])
	      	referencedCoordinate = None
	      	if targetGrid[coordinates[0][0]][coordinates[0][1]] == 1:
	      		print("It's a hit!!")
	      		targetGrid[coordinates[0][0]][coordinates[0][1]] = 0
	      		hitPoints.append(coordinates)
	      	else:
	      		print("It's a miss!!")

	      	if checkGrid(targetGrid) == 1:
	      		loop = 2
	      		print("Congratulations!! You've destroyed all of the opposing ships!!")
	      	else:
	      		#run computer's turn to hit uuser's ships. 
      elif status == 2: #coordinates has more than 1
      	if len(re.findall("(?:.*)(have)(?:.*)")) > 0:
      		if len(re.findall("(?:.*)(fire|target|shot|done)(?:.*)", userInput)) > 0:
      			if len(targetedPoints) > 0:
	      			print("You have already targeted the following coordinates: ")
	      			for i in range(len(targetedPoints)):
	      				print("Row: %d, Column: %d\n") % (targetedPoints[i][0], targetedPoints[i][1])
	      		else:
	      			print("You have not fired at any points yet.")
	      	elif len(re.findall("(?:.*)(ship|boat)(?:.*)", userInput)) > 0:
      			print("You're ships are stationed at the following coordinates: ")
  				for i in range(len(myShips)):
  					print("Row: %d, Column: %d\n") % (myShips[i][0], myShips[i][1])
  		else:
      		response = multipleTargetsResponses[random.randint(0, len(multipleTargetsResponses)) - 1]
      		print response
      elif len(re.findall("(?:.*)(last|past|previous|fire|gone|shoot|shot)(?:.*)", userInput)) > 0:
      	print("You have already targeted the following coordinates: ")
      	for i in range(len(targetedPoints)):
      		print("Row: %d, Column: %d\n") % (targetedPoints[i][0], targetedPoints[i][1])

      elif len(re.findall("(?:.*)(hit)(?:.*)", userInput)) > 0:
      	print("You have sunk ships at the following coordinates: ")
      	for i in range(len(hitPoints)):
      		print("Row: %d, Column: %d\n") % (hitPoints[i][0], hitPoints[i][1])

      elif len(re.findall("(?:.*)(my)(?:.*)", userInput)) > 0:
      	print("You're ships are stationed at the following coordinates: ")
      	for i in range(len(myShips)):
      		print("Row: %d, Column: %d\n") % (myShips[i][0], myShips[i][1])
      		#self.coordinates is list of user's ships coordinates. each coordinate entry is a 2 element array where [0] is row and [1] is column

      else:
      	print("Sorry, I didn't quite catch that. Can you try again??")

# Returns whether the target grid has been fully cleared and all ships have been destroyed. Returns 1 if all ships destroyed. 0 if ships still remain.
def checkGrid(self, targetGrid):
	for i in range(len(targetGrid)):
		for j in range(len(targetGrid[0])):
			if targetGrid[i][j] == 1:
				return 0
	return 1