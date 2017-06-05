import re
import string
import random
import numpy as math
from coord import *

def aligned(coordinates):
    if coordinates[0] == coordinates[1] or coordinates[0] == coordinates[2] or coordinates[1] == coordinates[2]:
        return False
    if coordinates[0][0] == coordinates[1][0] and coordinates[1][0] == coordinates[2][0]:
        return True
    if coordinates[0][1] == coordinates[1][1] and coordinates[1][1] == coordinates[2][1]:
        return True

def get_other_coord(coordinates):
	first_coord = coordinates[0]
	second_coord = coordinates[1]

	poss_coords = []

	if first_coord[0] == second_coord[0]:
		diff = math.abs(first_coord[1] - second_coord[1])
		if diff == 0:
			print 'ERROR, same coordinates'
		elif diff == 1:
			if second_coord[1] > first_coord[1]:
				poss_coords.append([first_coord[0], second_coord[1]+1])
				if first_coord[1]-1 > 0: poss_coords.append([first_coord[0], first_coord[1]-1])
			else:
				poss_coords.append([first_coord[0], first_coord[1]+1])
				if second_coord[1]-1 > 0: poss_coords.append([first_coord[0], second_coord[1]-1])
		elif diff == 2:
			if second_coord[1] > first_coord[1]:
				poss_coords.append([first_coord[0], first_coord[1]+1])
			else:
				poss_coords.append([first_coord[0], first_coord[1]-1])
		else: 
			print 'ERROR, coordinates don\'t align'

	elif first_coord[1] == second_coord[1]:
		diff = math.abs(first_coord[0] - second_coord[0])
		if diff == 0:
			print 'ERROR, same coordinates'
		elif diff == 1:
			if second_coord[0] > first_coord[0]:
				if first_coord[0]-1 > 0: poss_coords.append([first_coord[0]-1, second_coord[1]])
				poss_coords.append([second_coord[0]+1, first_coord[1]])
			elif second_coord[0] < first_coord[0]:
				poss_coords.append([first_coord[0]+1, second_coord[1]])
				if second_coord[0]-1 > 0: poss_coords.append([second_coord[0]-1, first_coord[1]])
		elif diff == 2:
			if second_coord[0] > first_coord[0]:
				poss_coords.append([first_coord[0]+1, first_coord[1]])
			else:
				poss_coords.append([first_coord[0]-1, first_coord[1]])
		else: 
			print 'ERROR, coordinates don\'t align'
	else:
		print 'THESE COORDINATES DON\'T ALIGN'
	return poss_coords
	

def parseShipPlacement(state):
	userInput = raw_input("Where would you like to place your ship?")
	userInput = userInput.lower()
	
	coordinates = []
	while len(coordinates) < 3:
		coord = get_coord(userInput)
		if len(coord) == 0:
			userInput = raw_input("Sorry. I didn't catch any coordinates in your response. Where would you like to place your ship?")

		elif len(coord) == 1:
			co = coord[0]
			coordinates.append(co)
			if len(coordinates)!=3: 
				userInput = raw_input("Great! Which other coordinates do you want this ship to cover?")
			else:
				print "Great! I'll see if we can place your ship at coordinates: " + str(coordinates)

		elif len(coord) == 2:
			if len(coordinates) > 1:
				userInput = raw_input("Sorry, you're providing too many coordinates. What's the last coordinate you'd like this ship to cover?")
			else:
				coordinates.extend(coord)
				print "Great! I'll see if we can place your ship at coordinates: " + str(coordinates)

		elif len(coord) == 3:
			if len(coordinates) != 0:
				userInput = raw_input("Sorry, you're providing too many coordinates. So far, your ship covers " + str(coordinates) + ". Which other coordinates do you want this ship to cover? ")
			else:
				coordinates.extend(coord)
				print "Great! I'll see if we can place your ship at coordinates: " + str(coordinates)

		else:
			userInput = raw_input("Sorry, you're providing too many coordinates. So far, your ship covers " + str(coordinates) + ". Which other coordinates do you want this ship to cover? ")
	
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

state = 0
c= parseShipPlacement(state)
print c