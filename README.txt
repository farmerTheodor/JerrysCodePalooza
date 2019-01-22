 _____                                      __                  
/\___ \                                    /\ \                 
\/__/\ \     __    _ __   _ __   __  __    \ \/      ____       
   _\ \ \  /'__`\ /\`'__\/\`'__\/\ \/\ \    \/      /',__\      
  /\ \_\ \/\  __/ \ \ \/ \ \ \/ \ \ \_\ \          /\__, `\     
  \ \____/\ \____\ \ \_\  \ \_\  \/`____ \         \/\____/     
   \/___/  \/____/  \/_/   \/_/   `/___/> \         \/___/      
                                     /\___/                     
                                     \/__/                      
 ____                __                                         
/\  _`\             /\ \                                        
\ \ \/\_\    ___    \_\ \      __                               
 \ \ \/_/_  / __`\  /'_` \   /'__`\                             
  \ \ \L\ \/\ \L\ \/\ \L\ \ /\  __/                             
   \ \____/\ \____/\ \___,_\\ \____\                            
    \/___/  \/___/  \/__,_ / \/____/                            
                                                                
                                                                
 ____               ___                                         
/\  _`\            /\_ \                                        
\ \ \L\ \   __     \//\ \      ___     ___    ____       __     
 \ \ ,__/ /'__`\     \ \ \    / __`\  / __`\ /\_ ,`\   /'__`\   
  \ \ \/ /\ \L\.\_    \_\ \_ /\ \L\ \/\ \L\ \\/_/  /_ /\ \L\.\_ 
   \ \_\ \ \__/.\_\   /\____\\ \____/\ \____/  /\____\\ \__/.\_\
    \/_/  \/__/\/_/   \/____/ \/___/  \/___/   \/____/ \/__/\/_/
                                                                
                                                                

(A+ for ascii please)

What is it:
A game where each player has one image and a maximum of ten methods to wreak destruction
on the opponent(s). Where things get interesting is that you yourself do not 
"play". Instead, you code inside the methods to create an "AI" and let the AI battle 
in your place. The AI has the ability to delete an opponents image one pixel at a 
time using a pre set command. The AI also has the ability to disable opponents methods.
The game is turn based and each bot is on a timer based on how long it takes to wipe an 
opponents board. However, how the game is won is also entirely up to you. You can modify
or create brand new rules before a match so that this game never gets stale.  


Things to note:
* for people not specializing in python:
	__variableName is a private variable
	abc is an abstract class
* composition can be found within the player class
* abstract classes can be found within the AI class
* while my program does not show too much event driven programming I do have it located
  in the funcions start game, select rules, and init players(game class)
* all GUIs can be found within the gameGUI folder
* A proper getter and setter can be found in the image class

Main OS: Ubuntu 18.4
Libraries used: tkinter, multiprocessing, abc and sys

How to run:
in the same folder this readme is located:
python3 game.py 


How to add your AI to the game

	Modify
* I created two AI which you can freely modify

	New
* create a class that extends AI
* impliment all methods to some degree
* import the class into game.py and player.py
* modify the method initPlayers() 


How to add rules to the game:

	Modify
* I created a set of rules which you can freely modify

	New
* create a class that extends Rules
* add all rules you want and be sure to impliment the abstract methods
* import the class into game.py
* modify the method selectRules() 


File structure:
main
	\	
	game.py(is the referee for the game and makes sure all rules are adhered to)
	gameComponents
		\
		image.py(is the image that each player has)
		player.py(calls all items related to him based on rules given to him by game.py)
	gameGUI
		\
		initGUI.py(is a selection screen)
		gameGUI.py(contains all graphical pieces for the game to run)
		playerGUI.py(contains all graphical pieces related to the player )
	gameRules
		\
		rules.py(abstract rules class)
		rulesTest.py(implimented rules.py)
	yourCode
		\
		baseAiClass.py(abstract AI class)
		fullAttack.py(implimented baseAiClass.py)



User stories(and how is achieved them):
As a computer programmer I can easily create an AI that interacts with the program(simple class based system with example code)
As a spectator I want to see what exactly is going on when two AI interact with each other(Added GUI) 
As a spectator I want the competition to end eventually(added a rule where you can time the game) 
As a competitor I want to have a fair and balanced game so that it is clearly the AI's fault and not the game(created the rule class so that you can modify the rules(and time it takes for certain commands) to your liking)


Things that I tried to do but failed:
* Instead of the class/method system style of bot, I wanted to use plain python code in which I would limit it not by time but python bytecode. The problem with this is that I could not figure out how you would stop at any given line. Because of this I then decided that I would use time. However, I still wanted to try take out individual lines of code. I soon realised that this would also lead to many errors as the only way to interact with the code was to use some sort of debugger or create my own using pyrasite. I decided that was wayyyyyyyy too much work. So I then decided to upscale lines of code into methods. This works very well and produces some nice gameplay.


Things not done: 
* Have not tested the game for more than two players. Should work but I just havent tested it yet.
* Have not tested having methods other than two. Should work though.
* Have not added score functionality in the GUI yet but still included them in the rules
* have not added a pause function or a step through function so you can analyze what your AI is doing
* have not given AI the ability to sense which methods our destroyed 
* have not limited the number of methods you can destroy
