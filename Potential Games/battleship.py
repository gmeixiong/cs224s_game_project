from random import randint

#initializing board

class State():
    def __init__(self):
        self.playerBoard = initializeBoard()
        self.cpuBoard = initializeBoard()
        self.totalShips = 3#per side
        self.history = []#player, (row, col), hit/miss

    def initializeBoard(self):
        board = []
        for x in range(5):
            board.append(["O"] * 5)
        return board

    def print_board(board):
        for row in board:
            print " ".join(row)

    def placeShip(coordinates, player):
        if player == 1:
            for coordinate in coordinates:
                self.cpuBoard[coordinate[0]][coordinate[1]] = "S"
        elif player == 0:
            for coordinate in coordinates:
                self.playerBoard[coordinate[0]][coordinate[1]] = "S"

    def fire(coordinate, player, cpu):
        row = coordinate[0]-1
        col = coordinate[1]-1
        if player == 1:
            if playerBoard[row][col] == "S":
                playerBoard[row][col] = "H"
                if cpu.firstHit == None:
                    cpu.firstHit = coordinate
                elif cpu.secondHit == None:
                    cpu.secondHit = coordinate
                else:
                    cpu.firstHit = None
                    cpu.secondHit = None
                self.history.append((1, coordinate, "H"))
            else:
                self.history.append((1, coordinate, "M"))
        elif player == 0:
            if cpuBoard[row][col] == "S":
                cpuBoard[row][col] = "H"
                self.history.append((0, coordinate, "H"))
            elif cpuBoard[row][col] == "O":
                cpuBoard[row][col] = "M"
                self.history.append((0, coordinate, "M"))
            else:
                wentHere = True
                #####They already went here


class CPU():
    def __init__(self):
        self.history = set([])
        self.firstHit = None
        self.secondHit = None

    def guess(self, board):
        if secondHit != None:
            guess = thirdGuess(board)
        elif firstHit != None:
            guess = secondGuess(board)
        else:
            guess = firstGuess(board)
        self.history.add(guess)
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
        guessIndex = possHits[randint(0, len(possHits-1))]
        guess = hitDict(guessIndex)
        while guess in self.history:
            guessIndex = possHits[randint(0, len(possHits-1))]
            guess = hitDict(guessIndex)
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

    def placeShips(self, state):
        shipPlacements = set([])
        for i in range(0, state.totalShips):
            restartNeeded = False
            shipProw = (random_row, random_col)
            possMasts = []
            hitDict = {
                1 : (self.shipProw[0]-1, self.shipProw[1]), 
                2 : (self.shipProw[0]+1, self.shipProw[1]), 
                3 : (self.shipProw[0], self.shipProw[1]-1), 
                4 : (self.shipProw[0], self.shipProw[1]+1), 
            }
            if self.shipProw[0]-1 >= 0:
                possMasts.append(1)
            if self.shipProw[0]+1 < len(board):
                possMasts.append(2)
            if self.shipProw[1]-1 >= 0:
                possMasts.append(3)
            if self.shipProw[1]+1 < len(board[0]):
                possMasts.append(4)
            guessIndex = possMasts[randint(0, len(possMasts-1))]
            shipMast = hitDict(guessIndex)
            while guess in shipPlacements:
                if possMasts.isEmpty():
                    restartNeeded = True
                    break
                guessIndex = possMasts[randint(0, len(possMasts-1))]
                shipMast = hitDict(guessIndex)
                possMasts.remove(guessIndex)
            if restartNeeded:
                i -= 1
                continue
            restartNeeded = True
            if self.shipProw[0] == self.shipMast[0]:
                if max(self.shipProw[1], self.shipMast[1]) + 1 < len(board[0]):
                    shipAft = (shipProw[0], max(self.shipProw[1], self.shipMast[1]) + 1)
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip([shipProw, shipMast, shipAft], 1)
                        restartNeeded = False
                if min(self.shipProw[1], self.shipMast[1]) - 1 < 0:
                    shipAft = (shipProw[0], min(self.shipProw[1], self.shipMast[1]) - 1)
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip([shipProw, shipMast, shipAft], 1)
                        restartNeeded = False
            if self.shipProw[1] == self.shipMast[1]:#should be the case
                if max(self.shipProw[0], self.shipMast[0]) + 1 < len(board):
                    shipAft = (max(self.shipProw[0], self.shipMast[0]) + 1, self.shipProw[1])
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip([shipProw, shipMast, shipAft], 1)
                        restartNeeded = False
                if min(self.shipProw[0], self.shipMast[0]) - 1 < 0:
                    shipAft = (min(self.shipProw[0], self.shipMast[0]) - 1, self.shipProw[1])
                    if shipAft not in shipPlacements:
                        shipPlacements.add(shipAft)
                        shipPlacements.add(shipProw)
                        shipPlacements.add(shipMast)
                        state.placeShip([shipProw, shipMast, shipAft], 1)
                        restartNeeded = False
            if restartNeeded:
                i -= 1
                continue





#starting the game and printing the board
print "Let's play Battleship!"
print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#asking the user for a guess
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        #warning if the guess is out of the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        
        #warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
        # Print turn and board again here
        print "Turn " + str(turn+1) + " out of 4." 
        print_board(board)

#if the user have made 4 tries, it's game over
if turn >= 3:
    print "Game Over"


def where(playerInput):
    if "their" in playerInput:
