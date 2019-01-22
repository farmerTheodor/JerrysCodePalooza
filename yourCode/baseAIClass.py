from abc import ABC, abstractmethod
from multiprocessing import Manager
import time
class AI(ABC):
 
    def __init__(self, boardSizeX, boardSizeY, opponents):
        super().__init__()
        self.__methods = [self.method1,self.method2,self.method3,self.method4,self.method5,self.method6,self.method7,self.method8,self.method9,self.method10]
        self.__methodDestroy = 0
        self.__methodResore = 0
        #shared with child classes 
        self.boardSizeX = boardSizeX
        self.boardSizeY = boardSizeY
        #copies purely for analytical stuff
        self.opponentsBoards = None
        self.yourBoard = None
        #list of numbers
        self.opponents = opponents
        
        #everything below is a shared value between processes
        self.__commands = None


    def changeOpponentMethod(self, opponentNum, methodNum, disable=True):
        #self.opponents[opponentNum] just to make sure you dont shoot yourself in the foot
        self.__commands.append(["changeOpponentMethod", self.opponents[opponentNum], methodNum, disable])
        time.sleep(self.__methodDestroy)

    def changeYourMethod(self, methodNum, disable=True):
        self.__commands.append(["changeYourMethod", methodNum, disable])
        time.sleep(self.__methodResore)

    def changeOpponentImage(self, opponentNum, x,y, val):
        self.__commands.append(["changeOpponentImage", self.opponents[opponentNum], x, y, val])
    
    def changeYourImage(self,x,y, val):
        self.__commands.append(["changeYourImage", x, y, val])

    def runMethod(self, commands, methodNum, opponentsBoards, yourBoard, methodRestorTime, methodDestroyTime ):
        start = time.time()
        self.__methodResore =methodRestorTime
        self.__methodDestroy = methodDestroyTime
        self.__commands = commands
        self.opponentsBoards = opponentsBoards
        self.yourBoard = yourBoard
        self.__methods[methodNum]()
        print(time.time() - start)

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    @abstractmethod
    def method3(self):
        pass

    @abstractmethod
    def method4(self):
        pass

    @abstractmethod
    def method5(self):
        pass

    @abstractmethod
    def method6(self):
        pass

    @abstractmethod
    def method7(self):
        pass

    @abstractmethod
    def method8(self):
        pass

    @abstractmethod
    def method9(self):
        pass

    @abstractmethod
    def method10(self):
        pass

