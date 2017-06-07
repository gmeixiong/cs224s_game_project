import re
import string


def get_coord(userInput):
      coordinates = []
      alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

      split = userInput.lower().split(" ")

      flag = False
      mergeFlag = False
      case2Flag = False

      for i in xrange(0, len(split)):
            wordlen = len(split[i])

            if split[i] in ['row']:
                  if flag == True:
                        flag = False
                        continue
                  coord = []
                  if i+3 < len(split):
                        row = split[i+1]
                        if split[i+2] in ['col', 'column']:
                              col = split[i+3]
                  row = row.strip('\'')
                  col = col.strip('\'')
                  coord.append(int(row))
                  coord.append(int(col))
                  flag = True
                  coordinates.append(coord)

            elif split[i] in ['col', 'column']:
                  if flag == True:
                        flag = False
                        continue
                  coord = []
                  if i+3 < len(split):
                        col = split[i+1]
                        if split[i+2] in ['row']:
                              row = split[i+3]
                  row = row.strip('\'')
                  col = col.strip('\'')
                  coord.append(int(row))
                  coord.append(int(col))
                  flag = True
                  coordinates.append(coord)

            elif split[i].startswith('row') and wordlen > 3:
                  if mergeFlag == True:
                        mergeFlag = False;
                        continue;

                  coord = []
                  if wordlen > 4:
                        case2Flag = True
                        row = split[i][3]
                        col = split[i][-1]
                  else:
                        row = split[i][-1]
                        if i + 1 < len(split):
                              col = split[i+1][-1]
                        mergeFlag = True

                  row = row.strip('\'')
                  col = col.strip('\'')
                  coord.append(int(row))
                  coord.append(int(col))

                  coordinates.append(coord)

            elif (split[i].startswith('col') or split[i].startswith('column')) and wordlen > 3:
                  if mergeFlag == True:
                        mergeFlag = False;
                        continue;

                  coord = []
                  if wordlen > 4:
                        case2Flag = True
                        if split[i][3].isalpha(): 
                              if wordlen > 7:
                                    col = split[i][6]
                                    row = split[i][-1]
                              else:
                                    col = split[i][-1]
                                    if i + 1 < len(split):
                                          row = split[i+1][-1]
                              mergeFlag = True
                        else:
                              col = split[i][3]
                              row = split[i][-1]
                  else:
                        col = split[i][-1]
                        if i + 1 < len(split):
                              row = split[i+1][-1]
                        mergeFlag = True

                  row = row.strip('\'')
                  col = col.strip('\'')
                  coord.append(int(row))
                  coord.append(int(col))

                  coordinates.append(coord)

      matches = re.findall("(?:\W|^|)[A-Ea-e]\s?[1-5](?:\W|$|)", userInput)
      if len(matches) == 1 and len(coordinates) < 1:
            matches[0] = matches[0].strip(" ")
            coord = []
            char = matches[0][0]
            row = alpha[char]
            col = int(matches[0][-1].strip('\''))
            coord.append(row)
            coord.append(col)
            coordinates.append(coord)
      else:
            matches = re.findall("(?:\W|^|)[A-Ea-e][1-5](?:\W|$|)", userInput)
            for i in xrange(len(matches)):
                  matches[i] = matches[i].strip(" ")
                  coord = []
                  char = matches[i][0]
                  row = alpha[char]
                  col = int(matches[i][-1].strip('\''))
                  coord.append(row)
                  coord.append(col)
                  coordinates.append(coord)

      matches1 = re.findall("(?:\W|^|)[1-5]\s?[A-Ea-e](?:\W|$|)", userInput)
      if len(matches1) == 1 and len(coordinates) < 1:
            matches1[0] = matches1[0].strip(" ")
            coord = []
            char = matches1[0][-1]
            row = alpha[char]
            col = int(matches1[0][0].strip('\''))
            coord.append(row)
            coord.append(col)
            coordinates.append(coord)
      else:
            if case2Flag == False:
                  matches1 = matches1 = re.findall("(?:\W|^|)[1-5][A-Ea-e](?:\W|$|)", userInput)
                  for i in xrange(len(matches1)):
                        matches1[i] = matches1[i].strip(" ")
                        coord = []
                        char = matches1[i][-1]
                        row = alpha[char]
                        col = int(matches1[i][0].strip('\''))
                        coord.append(row)
                        coord.append(col)
                        coordinates.append(coord)

      matches2 = re.findall("[1-5]\,[1-5]", userInput)
      if len(matches2) > 0:
            for i in xrange(len(matches2)):
                  coord = []
                  coord.append(int(matches2[i][0].strip('\'')))
                  coord.append(int(matches2[i][-1].strip('\'')))
                  coordinates.append(coord)

      # matches3 = re.findall("(?:\W|^)([1-5])\s([1-5])(?:\W|$)", userInput)
      # if len(matches3) > 0:
      #       for i in xrange(len(matches3)):
      #             coord =[]
      #             row = int(matches3[i][0].strip('\''))
      #             col = int(matches3[i][1].strip('\''))
      #             coord.append(row)
      #             coord.append(col)
      #             print "append4"
      #             coordinates.append(coord)

      return coordinates

# loop = 3
# while loop == 3:
#       print("---------------------------------------------------------")
#       print("Welcome to Battleships")
#       print("---------------------------------------------------------")

#       # First Screen and Input
#       userInput = raw_input(`)

#       coordinates = []

#       coordinates = get_coord(userInput)

#       print coordinates



