from random import randint
from fireMode import *
from placeShips import *
# from coord.py import *
#initializing board

class State():
    def __init__(self):
        self.playerBoard = self.initializeBoard()
        self.cpuBoard = self.initializeBoard()
        self.totalShips = 3#per side
        self.playerShips = set([])
        self.cpuShips = set([])
        self.history = []#player, (row, col), hit/miss
        self.targeted = set([])
        self.hit = set([])
        self.prevResult = None
        self.doubleHit = False
        self.doubleMiss = False

    def initializeBoard(self):
        board = []
        for x in range(5):
            board.append(["O"] * 5)
        return board

    def guessed(self, coordinate):#zero index
        coordinate = (coordinate[0], coordinate[1])
        if coordinate in self.targeted:
            print "dafsfa"
        else:
            print self.targeted
        return coordinate in self.targeted


    def placeShip(self, coordinates, player):
        print coordinates
        if player == 1:
            for coordinate in coordinates:
                self.cpuBoard[coordinate[0]][coordinate[1]] = "S"
                self.cpuShips.add(coordinate)
        elif player == 0:
            for coordinate in coordinates:
                self.playerBoard[coordinate[0]][coordinate[1]] = "S"
                self.playerShips.add(coordinate)


    def fire(self, coordinate, player, cpu):
        row = coordinate[0]-1
        col = coordinate[1]-1
        if player == 1:
            if self.playerBoard[row][col] == "S":
                self.playerBoard[row][col] = "H"
                if cpu.firstHit == None:
                    cpu.firstHit = coordinate
                elif cpu.secondHit == None:
                    cpu.secondHit = coordinate
                else:
                    cpu.firstHit = None
                    cpu.secondHit = None
                self.history.append((1, coordinate, "H"))
                self.playerShips.remove((row, col))
                return True
            else:
                self.history.append((1, coordinate, "M"))
                return False
        elif player == 0:
            self.targeted.add(coordinate)
            print "******"
            print self.targeted
            if self.cpuBoard[row][col] == "S":
                self.cpuBoard[row][col] = "H"
                self.history.append((0, coordinate, "H"))
                self.hit.add(coordinate)
                print self.cpuShips
                self.cpuShips.remove((row, col))
                return True
            elif self.cpuBoard[row][col] == "O":
                self.cpuBoard[row][col] = "M"
                self.history.append((0, coordinate, "M"))
                return False
            else:
                wentHere = True
                #####They already went here

    def checkWin(self):
        if len(state.playerShips) == 0:
            print "CPU won..."
            return True
        if len(state.cpuShips) == 0:
            print "Player Won!"
            return True
        return False

    def aligned(self, coordinates):
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

    def checkValid(self, coordinate):
        if coordinate[0] >= 1:
            if coordinate[0] <= len(self.playerBoard):
                if coordinate[1] >= 1:
                    if coordinate[1] <= len(self.playerBoard[0]):
                        return True
        return False

    def checkFree(self, coordinate):#only use for placements
        return not self.playerBoard == "S"


class CPU():
    def __init__(self):
        self.history = set([])
        self.firstHit = None
        self.secondHit = None

    def guess(self, board):
        if self.secondHit != None:
            guess = self.thirdGuess(board)
        elif self.firstHit != None:
            guess = self.secondGuess(board)
        else:
            guess = self.firstGuess(board)
        self.history.add(guess)
        guess = (guess[0]+1, guess[1]+1)
        return guess

    def firstGuess(self, board):
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[0]) - 1)
        while (row, col) in self.history:
            row = randint(0, len(board) - 1)
            col = randint(0, len(board[0]) - 1)
        return (row, col)

    def secondGuess(self, board):
        possHits = []
        hitDict = {
            1 : (self.firstHit[0]-1, self.firstHit[1]), 
            2 : (self.firstHit[0]+1, self.firstHit[1]), 
            3 : (self.firstHit[0], self.firstHit[1]-1), 
            4 : (self.firstHit[0], self.firstHit[1]+1), 
        }
        if self.firstHit[0]-1 >= 0:
            possHits.append(1)
        if self.firstHit[0]+1 < len(board):
            possHits.append(2)
        if self.firstHit[1]-1 >= 0:
            possHits.append(3)
        if self.firstHit[1]+1 < len(board[0]):
            possHits.append(4)
        guessIndex = possHits[randint(0, len(possHits)-1)]
        guess = hitDict[guessIndex]
        while guess in self.history:
            guessIndex = possHits[randint(0, len(possHits)-1)]
            guess = hitDict[guessIndex]
        return guess

    def thirdGuess(self, board):
        if self.firstHit[0] == self.secondHit[0]:
            if max(self.firstHit[1], self.secondHit[1]) + 1 < len(board[0]):
                guess = (firstHit[0], max(self.firstHit[1], self.secondHit[1]) + 1)
                if guess not in self.history:
                    return guess
            if min(self.firstHit[1], self.secondHit[1]) - 1 < 0:
                guess = (firstHit[0], min(self.firstHit[1], self.secondHit[1]) - 1)
                if guess not in self.history:
                    return guess
        if self.firstHit[1] == self.secondHit[1]:#should be the case
            if max(self.firstHit[0], self.secondHit[0]) + 1 < len(board):
                guess = (max(self.firstHit[0], self.secondHit[0]) + 1, self.firstHit[1])
                if guess not in self.history:
                    return guess
            if min(self.firstHit[0], self.secondHit[0]) - 1 < 0:
                guess = (min(self.firstHit[0], self.secondHit[0]) - 1, self.firstHit[1])
                if guess not in self.history:
                    return guess
        return self.firstGuess(self,board)

    def placeShips(self, state):
        board = state.cpuBoard
        shipPlacements = set([])
        state.cpuShips = set([])
        for i in range(0, state.totalShips):
            restartNeeded = False
            shipProw = (self.random_row(state.cpuBoard), self.random_col(state.cpuBoard))
            possMasts = []
            hitDict = {
                1 : (shipProw[0]-1, shipProw[1]), 
                2 : (shipProw[0]+1, shipProw[1]), 
                3 : (shipProw[0], shipProw[1]-1), 
                4 : (shipProw[0], shipProw[1]+1), 
            }
            if shipProw[0]-1 >= 0:
                possMasts.append(1)
            if shipProw[0]+1 < len(board):
                possMasts.append(2)
            if shipProw[1]-1 >= 0:
                possMasts.append(3)
            if shipProw[1]+1 < len(board[0]):
                possMasts.append(4)
            guessIndex = possMasts[randint(0, len(possMasts)-1)]
            shipMast = hitDict[guessIndex]
            while shipMast in shipPlacements:
                possMasts.remove(guessIndex)
                if len(possMasts) == 0:
                    restartNeeded = True
                    break
                guessIndex = possMasts[randint(0, len(possMasts)-1)]
                shipMast = hitDict[guessIndex]
            if restartNeeded:
                print "restart"
                possMasts = []
                self.placeShips(state)
                return
                i -= 1
                continue
            restartNeeded = True
            if shipProw[0] == shipMast[0]:
                if max(shipProw[1], shipMast[1]) + 1 < len(board[0]):
                    shipAft = (shipProw[0], max(shipProw[1], shipMast[1]) + 1)
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip((shipProw, shipMast, shipAft), 1)
                        restartNeeded = False
                        continue
                if min(shipProw[1], shipMast[1]) - 1 >= 0:
                    shipAft = (shipProw[0], min(shipProw[1], shipMast[1]) - 1)
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip((shipProw, shipMast, shipAft), 1)
                        restartNeeded = False
                        continue
            if shipProw[1] == shipMast[1]:#should be the case
                if max(shipProw[0], shipMast[0]) + 1 < len(board):
                    shipAft = (max(shipProw[0], shipMast[0]) + 1, shipProw[1])
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip((shipProw, shipMast, shipAft), 1)
                        restartNeeded = False
                        continue
                if min(shipProw[0], shipMast[0]) - 1 >= 0:
                    shipAft = (min(shipProw[0], shipMast[0]) - 1, shipProw[1])
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip((shipProw, shipMast, shipAft), 1)
                        restartNeeded = False
                        continue
            if restartNeeded:
                # possMasts = []
                print "restart"
                self.placeShips(state)
                return
                i -= 1

    def random_row(self, board):
        return randint(0, len(board) - 1)

    def random_col(self, board):
        return randint(0, len(board[0]) - 1)





#starting the game and printing the board
print "Let's play Battleship!"

state = State()
cpu = CPU()
cpu.placeShips(state)
print state.cpuShips

for i in range(0, state.totalShips):
    # inputList = raw_input("Where do you want your first ship to be?").split()
    # state.placeShip([(int(inputList[0]), int(inputList[1])), (int(inputList[2]), int(inputList[3])), (int(inputList[4]), int(inputList[5]))], 0)
    coordinates = parseShipPlacement(state)
    for i in range(0, len(coordinates)):
        coordinate = coordinates[i]
        coordinates[i] = (coordinate[0]-1, coordinate[1]-1)
        print coordinate
    coordinates = (coordinates[0], coordinates[1], coordinates[2])
    state.placeShip(coordinates, 0)
    print coordinates
    print state.playerShips
#defining where the ship is



#asking the user for a guess
while True:
    # guess_row = int(raw_input("Guess Row:"))
    # guess_col = int(raw_input("Guess Col:"))
    #hit = state.fire((guess_row, guess_col), 0, cpu)
    coordinate = parseFireInput(state)
    hit = state.fire((coordinate[0], coordinate[1]), 0, cpu)
    if hit:
        print "Hit!"
        if state.prevResult == "hit":
            state.doubleHit = True
        state.prevResult = "hit"
        state.doubleMiss = False
        if state.checkWin():
            print "Game Over"
            break
    else:
        print "Miss..."
        if state.prevResult == "miss":
            state.doubleMiss = True
        state.prevResult = "miss"
        state.doubleHit = False
    cpuhit = state.fire(cpu.guess(state.playerBoard), 1, cpu)
    if cpuhit:
        print "Hit! from the CPU"
        if state.checkWin():
            print "Game Over"
            break
    else:
        print "Miss... from the CPU"



    # # if the user's right, the game ends
    # if guess_row == ship_row and guess_col == ship_col:
    #     print "Congratulations! You sunk my battleship!"
    #     break
    # else:
    #     #warning if the guess is out of the board
    #     if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
    #         print "Oops, that's not even in the ocean."
        
    #     #warning if the guess was already made
    #     elif(board[guess_row][guess_col] == "X"):
    #         print "You guessed that one already."
        
    #     #if the guess is wrong, mark the point with an X and start again
    #     else:
    #         print "You missed my battleship!"
    #         board[guess_row][guess_col] = "X"
        
    #     # Print turn and board again here
    #     print "Turn " + str(turn+1) + " out of 4." 
    #     print_board(board)

#if the user have made 4 tries, it's game over
# if turn >= 3:
#     print "Game Over"


