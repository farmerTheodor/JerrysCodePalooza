from tkinter import *
import sys
sys.path.insert(0, './gameGUI')
from playerGui import PlayerGUI

class GameGUI(Frame):
	"""docstring for GameGUI"""
	def __init__(self, parent, boardX, boardY, numPlayers):
		super(GameGUI, self).__init__(parent)
		self.__numPlayers = numPlayers
		self.__players = []
		self.__codeBoxes = []
		for x in range(0,numPlayers):
			playerFrame = PlayerGUI(self,boardX, boardY, "player " + str(x + 1))
			playerFrame.pack(side=LEFT)
			self.__players.append(playerFrame)


	def updateCodeList(code=["no code"], playerNum = 0):
		codeList = self.__codeBoxes[playerNum]
		for line in code:
			codeList.insert(END, line)

	def updateBoard(self, imageOf, playerNum ):
		self.__players[playerNum].updateImage(imageOf)

	def updateCommand(self, codeOf, playerNum):
		self.__players[playerNum].updateCommand(codeOf)		



		