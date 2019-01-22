from tkinter import *

class PlayerGUI(Frame):
	"""docstring for PlayerGUI"""
	def __init__(self, parent, boardX, boardY, nameOf):
		super(PlayerGUI, self).__init__(parent)
		self.__boardX = boardX
		self.__boardY = boardY
		imageFrame, self.__imgFrames = self.__createImage(self)
		imageFrame.pack()
		name = Label(self, text=nameOf)
		name.pack()
		code, self.__codeList = self.__createCodeList(self)
		code.pack()
		
	def __createImage(self, root):
		imageFrame = Frame(root)
		widHi = 20
		imgFrames = []
		for x in range(0,self.__boardX):
			imgFrames.append([])
			for y in range(0, self.__boardY):
				frameOf = Frame(imageFrame, width=widHi, height=widHi, background="Red")
				frameOf.grid(row=y, column=x)
				imgFrames[x].append(frameOf)

		return imageFrame, imgFrames

	def __createCodeList(self, root):
		widHi = self.__boardX * 200
		listFrame = Frame(root, width = widHi, height=widHi)
		code = Listbox(listFrame )
		
		code.pack(fill=BOTH)
		#self.__codeBoxes.append(code)
		return listFrame, code

	def updateImage(self,imageOf):
		for x in range(0,self.__boardX):
			for y in range(0, self.__boardY):
				if(imageOf[x][y] == 1):
					self.__imgFrames[x][y].configure(background="Red")
				else:
					self.__imgFrames[x][y].configure(background="Blue")
	
	def updateCommand(self, codeOf):
		self.__codeList.delete(0, END)
		for line in codeOf:
			self.__codeList.insert(END, line)