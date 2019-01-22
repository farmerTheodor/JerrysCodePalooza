
class Image(object):
	"""docstring for Image"""
	def __init__(self, boardX, boardY):
		super(Image, self).__init__()
		self.__boardX = boardX
		self.__boardY = boardY
		self.__imageData = []
		for x in range(0,self.__boardX):
			self.__imageData.append([])
			for y in range(0, self.__boardY):
				self.__imageData[x].append(1)

	def updateImage(self,x,y, val):
		self.__imageData[x][y] = val


	def returnImageData(self):
		return self.__imageData.copy()


		