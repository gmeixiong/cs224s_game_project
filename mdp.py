class BlackjackMDP(util.MDP):
    def __init__(self, locations):
        """
        cardValues: array of card values for each card type
        multiplicity: number of each card type
        threshold: maximum total before going bust
        peekCost: how much it costs to peek at the next card
        """
        self.locations = locations

    # Return the start state.
    # Look at this function to learn about the state representation.
    # Name, Location, Inventory, History, Response
    def startState(self):
        return ("????", self.locations[0], {}, [], "Hello, and Welcome to our 221 Project! Would you like to begin?")  # total, next card (if any), multiplicity for each card

    # Return set of actions possible from |state|.
    # You do not need to modify this function.
    # All logic for dealing with end states should be done in succAndProbReward
    # Ask for name, Ask for confirmation, Give Location Details, Show Inventory
    def actions(self, state):
        return ["Name?", "Confirmation?", "Location", "Inventory"]


    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.  Indicate a terminal state (after quitting or
    # busting) by setting the deck to None. 
    # When the probability is 0 for a particular transition, don't include that 
    # in the list returned by succAndProbReward.
    def succAndProbReward(self, state, action):
        # BEGIN_YOUR_CODE (our solution is 53 lines of code, but don't worry if you deviate from this)
        #raise Exception("Not implemented yet")
        actionList = []
        if action = "Name?":
            response = generateNameAsk()
            newState = (state[0], state[1], state[2], state[3], response)
            if state[0] == "????":
                actionList.append((newState, 1, reward))
        if action = "Confirmation?"
            response = generateConfirmationAsk()
            newState = 


        # END_YOUR_CODE

    def discount(self):
        return 1