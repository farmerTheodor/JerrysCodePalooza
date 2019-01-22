from tkinter import *


class InitGUI(Frame):
	"""docstring for initGUI"""
	def __init__(self, parent, ruleSets = ["testRules"]):
		super(InitGUI, self).__init__(parent)
		self.__selectedRule = ""
		self.__parent = parent
		self.__var = StringVar(self)
		self.__var.set(ruleSets[0])
		#passes in the different options via the * character
		options = OptionMenu( self, self.__var, *ruleSets)
		options.pack()
		goButton = Button(self, text="ok", command=self.selectRuleSet)
		goButton.pack()

	def selectRuleSet(self):
		self.__selectedRule = self.__var.get()
		self.__parent.quit()


	def returnRuleSet(self):
		return self.__selectedRule