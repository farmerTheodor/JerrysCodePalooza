from abc import ABC, abstractmethod

class Rules(ABC):
 
    def __init__(self):
        super().__init__()
        #things start slow at 20*20
        self.__boardSizeX = 0
        self.__boardSizeY = 0
        self.__numPlayers = 0
        #max is ten
        self.__numMethods = 0
        #all stuff below are a fraction of the average time it takes to change a board from full on to off
        #balance stuff will impliment if I have time(had time)
        self.__timeDelayDestroyMethod = 1
        self.__timeDelayRestoreMethod = 1
        self.__timeModifier = 1




    @abstractmethod
    def turnOrder(self, players):
        pass

    @abstractmethod
    def methodOrder(self):
        pass

    @abstractmethod
    def calculateScore(self, image = "", code = ""):
    	pass

    @abstractmethod
    def isEnd(self, playersAlive, time):
    	pass

    @abstractmethod
    def isDead(self, playerIs):
        pass

    @abstractmethod
    def verifyCode(self, code):
    	pass

    def returnBoardSizeX(self):
    	return self.__boardSizeX

    def returnBoardSizeY(self):
    	return self.__boardSizeY

    def returnNumPlayers(self):
    	return self.__numPlayers

    def returnTimeModifier(self):
        return self.__timeModifier

    def returnNumMethods(self):
        return self.__numMethods
 
    def returnTimeDelayDestroyMethod(self):
        return self.__timeDelayDestroyMethod

    def returnTimeDelayRestoreMethod(self):
        return self.__timeDelayRestoreMethod