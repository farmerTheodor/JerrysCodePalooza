import sys
from tkinter import *
import time
from multiprocessing import Process, Manager
sys.path.insert(0, './gameGUI')
sys.path.insert(0, './gameComponents')
sys.path.insert(0, './gameRules')
sys.path.insert(0, './yourCode')
from rules import Rules
from rulesTest import RulesTest
from initGui import InitGUI
from gameGui import GameGUI
from player import Player
from mixAttackDef import Mixed
from fullAttack import Attack

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		super(Game, self).__init__()
		self.__rules = self.__selectRules()
		self.__players = self.__initPlayers()
		#so that two computers roughly behave the same(probably wont work but thats because I dont have enough computers)
		self.__timePerTurn = self.__calcTimePerTurn()
		self.__gui = None
		
		

	def __mockTurn(self,commands, boardX, boardY):
		#calculates average time to wipe out another players board
		for x in boardX:
				for y in boardY:
					commands.append(["a",y,x,1])

	def __calcTimePerTurn(self):
		#creates mock processes to determine speed of computer and thus the speed of a turn
		#you can modify how long the turn takes within the rules class but this is base
		timeToKill = 0
		numRepeat = 100
		manager = Manager()

		for i in range(1,numRepeat):
			boardX = range(0, self.__rules.returnBoardSizeX())
			boardY = range(0, self.__rules.returnBoardSizeY())
			#we use this list even though we dont have to retrieve anything because it is slower than a regular list
			listOfCommands = manager.list()
			p = Process(target=self.__mockTurn, args=(listOfCommands, boardX, boardY,))
			
			start = time.time()
			p.start()
			p.join()
			end = time.time()

			timeToKill = timeToKill + (end - start)
		print(timeToKill/numRepeat)
		return timeToKill/numRepeat

	def __initPlayers(self):
		listOfPlayers = []
		for x in range(0,self.__rules.returnNumPlayers()):
			root = Tk()
			#___add some name here to include your class ___
			selectAi = InitGUI(root, ["fullAttack", "mixed"])

			selectAi.pack()
			root.mainloop()
			aiToUse = selectAi.returnRuleSet()
			root.destroy()

			AI = None
			opponents = list(range(0,self.__rules.returnNumPlayers()))
			opponents.remove(x)
			
			#___add a statement to create your object If your class was selected___
			if(aiToUse == "fullAttack"):
				AI = Attack(self.__rules.returnBoardSizeX(), self.__rules.returnBoardSizeY(), opponents)	
			else:
				AI = Mixed(self.__rules.returnBoardSizeX(),self.__rules.returnBoardSizeY(), opponents)

			listOfPlayers.append(Player(self.__rules.returnBoardSizeX(), self.__rules.returnBoardSizeY(), AI, self.__rules.returnNumMethods()))

		return listOfPlayers

	def __changePlayerMethod(self, playerNum, methodNum, disable=True):
		self.__players[playerNum].updateUsableMethod(methodNum, disable)

	def __changePlayerImage(self, playerNum, x,y, val):
		self.__players[playerNum].updateCurImage(x,y,val)


	def __executeTurn(self, playerNum):
		print("executing turn for player ", playerNum+1)
		opponentsBoards = []
		for player in self.__players:
			opponentsBoards.append(player.returnCurImage())
		opponentsBoards.pop(playerNum)
		listOfCommands = self.__players[playerNum].runAI(self.__rules.returnTimeModifier() * self.__timePerTurn, opponentsBoards,
		 	self.__rules.returnTimeDelayDestroyMethod(),
		 	self.__rules.returnTimeDelayRestoreMethod())
		#generates the command within the AI and executes the commands here
		for command in listOfCommands:
			if(command[0] == "changeOpponentMethod"):
				self.__changePlayerMethod(command[1], command[2], command[3])
			elif(command[0] == "changeYourMethod"):
				self.__changePlayerMethod(playerNum, command[1], command[2])
			elif(command[0] == "changeOpponentImage"):
				self.__changePlayerImage(command[1], command[2], command[3], command[4])
			elif(command[0] == "changeYourImage"):
				self.__changePlayerImage(playerNum, command[1], command[2], command[3])
		#returns list of commands for later gui update
		return listOfCommands

	def __updateGUI(self, commands):
		#while I know this is not pythonic at all it increases readability a little bit
		for playerNum in range(0,self.__rules.returnNumPlayers()):
				self.__gui.updateBoard(self.__players[playerNum].returnCurImage(), playerNum)
				self.__gui.updateCommand(commands[playerNum], playerNum)
		#call to actually update the gui
		self.__gui.update()
		
	def fight(self):
		#inits array of size numPlayers
		playersLeft = [True] * self.__rules.returnNumPlayers()
		totalTime = 0
		#enters game loop
		while not self.__rules.isEnd(playersLeft, totalTime):
			print("starting another round")
			start = time.time()
			listOfCommands = []
			for playerNum in self.__rules.turnOrder():

				if( self.__rules.isDead(self.__players[playerNum])):
					playersLeft[playerNum] = False
					listOfCommands.append(["KO"])
					print("player died")
				else:
					listOfCommands.append(self.__executeTurn(playerNum))
			end = time.time()
			totalTime = totalTime + (end - start)
			#update here and not during the timer so that it does not affect game time 
			self.__updateGUI(listOfCommands)
			

	def restart(self):
		self.__players = self.__initPlayers()
		self.__updateGUI([[],[]])


	def startGame(self):
		root = Tk()
		self.__gui = GameGUI(root,self.__rules.returnBoardSizeX(),
			 self.__rules.returnBoardSizeY(),
			 self.__rules.returnNumPlayers())
		self.__gui.pack()

		goBtn = Button(root, text="Fight!", command=self.fight)
		restart = Button(root, text="restart", command=self.restart)
		goBtn.pack()
		restart.pack()
		
		root.mainloop()
		



	def __selectRules(self):
		root = Tk()
		#add name for rules here
		selectRules = InitGUI(root, ["rulesTest", "no thanks I would rather not enter the rumble"])
		selectRules.pack()
		root.mainloop()
		ruleToUse = selectRules.returnRuleSet()
		root.destroy()
		#add if statement for your rules
		if(ruleToUse == "rulesTest"):
			return RulesTest()	
		quit()
		return None


def main():
	newGame = Game()
	newGame.startGame()


if __name__ == '__main__':
	main()
		
