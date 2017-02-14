# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[
            index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # print "newScaredTimes", newScaredTimes
        # print successorGameState.getCapsules()

        newGhostPos = newGhostStates[0].getPosition()
        ghost_dist = ghost_distance(newPos, newGhostPos)
        capsules = successorGameState.getCapsules()
        # food_dist = food_distance(newPos, newFood)

        # approach 1: 2/4 win = 10, average < 500
        # if ghost_dist <= 1:
        #     return -999999
        # return -food_num(newFood)

        # approach 2: 2/4 win = 10, average < 500 but close to 500
        # if newScaredTimes[0] == 0:
        #     if ghost_dist <= 1:
        #         return -999999
        # return -food_num(newFood) -capsule_distance(newPos, capsules)

        # final approach: 4/4 win = 10, average = 1310.5
        if newScaredTimes[0] == 0:
            if ghost_dist <= 1:
                return -999999
        return -food_distance(newPos, newFood) * .01 - food_num(newFood) - capsule_distance(newPos, capsules)


def distance(xy1, xy2):
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


def capsule_distance(position, capsules):
    if capsules:
        return distance(position, capsules[0])
    else:
        return 0


def ghost_distance(position, ghost_position):
    xy1 = position
    xy2 = ghost_position
    return distance(xy1, xy2)


def food_num(food):
    return len(food.asList())


def food_distance(position, food):

    num_food = len(food.asList())
    if num_food == 0:
        return 0
    else:
        return min([distance(position, food_position) for food_position in food.asList()])


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    # is this a terminal state
    def isTerminal(self, gameState, depth, agentIndex):
        return depth == self.depth or gameState.isWin() or gameState.isLose()

    # is this agent pacman
    def isPacman(self, gameState, agentIndex):
        return agentIndex % gameState.getNumAgents() == self.index


class MinimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
        return max(gameState.getLegalActions(self.index),
                   key = lambda action: self.minMaxValueAction(gameState, action))

    def minMaxValue(self, gameState, depth, agentIndex):

        if self.isPacman(gameState, agentIndex) and agentIndex > 0: 
            return self.minMaxValue(gameState, depth + 1, self.index)  
        
        if self.isTerminal(gameState, depth, agentIndex):
            return self.evaluationFunction(gameState)

        if self.isPacman(gameState, agentIndex):
            return self.maxValue(gameState, depth, agentIndex)  
        else:
            return self.minValue(gameState, depth, agentIndex)

    # -------------- helper functions --------------

    def minMaxValueAction(self, gameState, action):
        successorGameState = gameState.generateSuccessor(self.index, action)
        return self.minMaxValue(successorGameState, depth=0, agentIndex=1)

    def  minValue(self, gameState, depth, agentIndex):
        return min(self.successorValues(gameState, depth, agentIndex))

    def  maxValue(self, gameState, depth, agentIndex):
        return max(self.successorValues(gameState, depth, agentIndex))

    def successorValues(self, gameState, depth, agentIndex):
        legalActions = gameState.getLegalActions(agentIndex)
        return [self.minMaxValue(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1) 
                            for action in legalActions]


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        return max(gameState.getLegalActions(self.index),
                   key = lambda action: self.expectMaxValueAction(gameState, action))

    def expectMaxValue(self, gameState, depth, agentIndex):

        if self.isPacman(gameState, agentIndex) and agentIndex > 0: 
            return self.expectMaxValue(gameState, depth + 1, self.index)  
        
        if self.isTerminal(gameState, depth, agentIndex):
            return self.evaluationFunction(gameState)

        if self.isPacman(gameState, agentIndex):
            return self.maxValue(gameState, depth, agentIndex)  
        else:
            return self.expectValue(gameState, depth, agentIndex)

    # -------------- helper functions --------------
    
    def expectMaxValueAction(self, gameState, action):
        successorGameState = gameState.generateSuccessor(self.index, action)
        return self.expectMaxValue(successorGameState, depth=0, agentIndex=1)

    def  expectValue(self, gameState, depth, agentIndex):
        successorValues = self.successorValues(gameState, depth, agentIndex)
        return sum(successorValues) / len(successorValues)

    def  maxValue(self, gameState, depth, agentIndex):
        return max(self.successorValues(gameState, depth, agentIndex))

    def successorValues(self, gameState, depth, agentIndex):
        legalActions = gameState.getLegalActions(agentIndex)
        return [self.expectMaxValue(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1) 
                            for action in legalActions]


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPos = currentGameState.getPacmanPosition()

    food = currentGameState.getFood()
    capsules = currentGameState.getCapsules()
    return currentGameState.getScore() - 10 * capsuleDistancePlan(pacmanPos, capsules) - foodDistPlan(pacmanPos, food)

def capsuleDistancePlan(position, capsules):
    if capsules:
        return sum([ distance(position, capsule) for capsule in capsules ])
    else:
        return 0

def foodDistPlan(position, food):

    numFood = len(food.asList())
    if numFood == 0:
        return 0
    else:
        return min([distance(position, foodPos) for foodPos in food.asList()])

# Abbreviation
better = betterEvaluationFunction
















