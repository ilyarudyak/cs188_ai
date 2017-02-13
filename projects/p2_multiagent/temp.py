        bestActionIndex = max(gameState.getLegalActions(agentIndex))

        return random.choice(legal_states)
        
    def getActionHelper(self, gameState, depth):

        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        for agentIndex in range(gameState.getNumAgents()):
            if agentIndex == self.index:
                return maxValue(gameState, agentIndex, depth)
            else:
                return minValue(gameState, agentIndex, depth)


    def maxValue(self, gameState, agentIndex, depth):
        v = -999999
        for action in gameState.getLegalActions(agentIndex):
            for successor in gameState.generateSuccessor(agentIndex, action):
                v = max(v, getActionHelper(successor, depth + 1))
        return v


    def minValue(self, gameState, agentIndex, depth):
        v = +999999
        for action in gameState.getLegalActions(agentIndex):
            for successor in gameState.generateSuccessor(agentIndex, action):
                v = min(v, getActionHelper(successor, depth + 1))
        return v