import sys
from multiprocessing import Process, Manager
import time
sys.path.insert(0, './gameComponents')
sys.path.insert(0, './yourCode')
from fullAttack import Attack
from mixAttackDef import Mixed
from image import Image


class Player(object):
	"""docstring for Player"""
	def __init__(self, boardX, boardY, AI, numMethods):
		super(Player, self).__init__()
		self.__curImage = Image(boardX, boardY)
		self.__oldImage = Image(boardX, boardY)
		self.__curAI = AI
		self.__curMethodNum = 0
		#inits an array of size numMethods
		self.__methodsBlocked = [True] * numMethods
		

	def runAI(self, timePerTurn, copyOpponentsBoards, methodRestore, methodDestroy):
		manager = Manager()
		listOfCommands = manager.list()
		methodNotExecuted = True
		while methodNotExecuted :
			methodNum = self.__curMethodNum % len(self.__methodsBlocked)
			self.__curMethodNum  = self.__curMethodNum + 1
			if(self.__methodsBlocked[methodNum]):
				#executes a script for a set amount of time before killing it
				p = Process(target=self.__curAI.runMethod, args=(listOfCommands,methodNum, copyOpponentsBoards, self.returnCurImage(),methodRestore, methodDestroy,))
				methodNotExecuted = False
				p.start()
				time.sleep(timePerTurn)
				p.terminate()


		print(listOfCommands)
		return listOfCommands

	def updateUsableMethod(self, methodNum, disable=False):
		self.__methodsBlocked[methodNum] = disable

	def updateCurImage(self,x,y,val):
		self.__curImage.updateImage(x,y,val)

	def returnMethodsBlocked(self):
		return self.__methodsBlocked

	def returnCurImage(self):
		return self.__curImage.returnImageData()

	def returnOldImage(self):
		return self.__oldImage.returnImageData()

