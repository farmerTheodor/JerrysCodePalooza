import sys

sys.path.insert(0, './yourCode')
from baseAIClass import AI

class Attack(AI):
	"""docstring for Attack"""
	def __init__(self, boardSizeX, boardSizeY, opponents):
		super(Attack, self).__init__(boardSizeX, boardSizeY, opponents)
		
	def method1(self):
		for x in range(0,2):
			self.changeOpponentMethod(0,x,False)
		
	def method2(self):
		for x in range(2,4):
			self.changeOpponentMethod(0,x,False)

	def method3(self):
		for x in range(4,6):
			self.changeOpponentMethod(0,x,False)

	def method4(self):
		for x in range(6,8):
			self.changeOpponentMethod(0,x,False)

	def method5(self):
		for x in range(8,10):
			self.changeOpponentMethod(0,x,False)

	def method6(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method7(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method8(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method9(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

	def method10(self):
		for x in range(0,self.boardSizeX):
			for y in range(0,self.boardSizeY):
				self.changeOpponentImage(0,x,y,0)

