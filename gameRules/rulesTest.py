import sys
sys.path.insert(0, './gameRules')
sys.path.insert(0, './gameComponents')
from player import Player
from rules import Rules

class RulesTest(Rules):
	"""docstring for RulesTest
		two player game

	"""
	def __init__(self):
		super(RulesTest, self).__init__()
		self._Rules__boardSizeX = 20
		self._Rules__boardSizeY = 20
		self._Rules__numPlayers = 2
		self._Rules__numMethods = 10
		self._Rules__timeModifier = 1
		self.__timeToRun = 10

	
	def turnOrder(self, players=None):
		return [0,1]
	
	def methodOrder(self):
		return range(0,self._Rules__numMethods)

  
	def calculateScore(self, image, origImage, code):
		score = 0
		for x in range(1,self.__boardSizeX):
			for y in range(1,self.__boardSizeY):
				if(image[x][y] == origImage[x][y]):
					score = score + 1
		return score

  
	def isEnd(self, playersAlive, time):
		if(time > self.__timeToRun):
			return True
		lastMan = 0
		for player in playersAlive:
			lastMan = lastMan + int(player)
		print(lastMan)
		return lastMan <= 1


	def isDead(self, playerIs):
		image = playerIs.returnCurImage()
		origImage = playerIs.returnOldImage()
		score = 0
		for x in range(1,self._Rules__boardSizeX):
			for y in range(1,self._Rules__boardSizeY):
				if(image[x][y] == origImage[x][y]):
					score = score + 1
		if(score == 0):
			return True
		return not True in playerIs.returnMethodsBlocked()


	def verifyCode(self, code):
		pass
