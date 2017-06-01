import re
import string

loop = 3
while loop == 3:
      print("---------------------------------------------------------")
      print("Welcome to Battleships")
      print("Note: please type all our reponses in quotes.")
      print("---------------------------------------------------------")

      # First Screen and Input
      userInput = input("Where would you like to place your ship? ")

      coordinates = []

      matches = re.findall("[A-Ea-e][1-5]", userInput)
      if len(matches) > 0:
            for i in xrange(len(matches)):
                  coordinates.append(matches[i])

      matches1 = re.findall("[1-5][A-Ea-e]", userInput)
      if len(matches1) > 0:
            for i in xrange(len(matches1)):
                  reverse = matches1[i][-1]
                  reverse += matches1[i][0]
                  matches1[i] = reverse
                  coordinates.append(matches1[i])

      matches2 = re.findall("[1-5]\,[1-5]", userInput)
      if len(matches2) > 0:
            for i in xrange(len(matches2)):
                  coordinates.append(matches2[i])

      matches3 = re.findall("(?:\W|^)([1-5])\s([1-5])(?:\W|$)", userInput)
      if len(matches3) > 0:
            for i in xrange(len(matches3)):
                  row = matches3[i][0]
                  col = matches3[i][1]
                  matches3[i] = row + "," + col
                  coordinates.append(matches3[i])

      split = userInput.lower().split()
      for i in xrange(len(split)):
            if split[i] in ['row']:
                  if i+3 < len(split):
                        row = split[i+1]
                        if split[i+2] in ['col', 'column']:
                              col = split[i+3]
                  coord = row + "," + col
                  i = i+3
            elif split[i] in ['col', 'column']:
                  if i+3 < len(split):
                        col = split[i+1]
                        if split[i+2] in ['row']:
                              row = split[i+3]
                  coord = row + "," + col
                  i = i+3
                  coordinates.append(coord)

      print coordinates

