import sys
sys.path.insert(0, './yourCode')
from baseAIClass import AI

class Mixed(AI):
	"""docstring for Attack"""
	def __init__(self,boardSizeX, boardSizeY, opponents):
		super(Mixed, self).__init__(boardSizeX, boardSizeY, opponents)
		
	def method1(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method2(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeYourImage(x,y,1)

	def method3(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method4(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeYourImage(x,y,1)

	def method5(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method6(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeYourImage(x,y,1)

	def method7(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method8(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeYourImage(x,y,1)

	def method9(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method10(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeYourImage(x,y,1)

