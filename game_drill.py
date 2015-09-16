# game_drill.py by gail hedberg - jun 14, 2015
# updated version of this game for class project, original version found at:
#  https://www.youtube.com/watch?v=1ELfaJcUWOQ

import time

class GameLoot:
    def __init__(self):
        self.apples = 0
        self.gold = 0
        self.play = 'N'

    def addAnApple(self):
        self.apples = self.apples + 1
        
    def getApples(self):
        return self.apples

    def hasApples(self):
        if self.apples == 0:
            return False
        else: return True

    def sellApples(self):
        self.gold = self.gold + (self.apples * 10)
        self.apples = 0

    def getGold(self):
        return self.gold

    def setPlay(self, play):
        self.play = play.upper()
 #       print('play is ', self.play)

    def playGame(self):
        if self.play == 'Y':
            return True
        else:
            return False
        
    def isAWinner(self):
        if self.gold > 57:
            return True
        else : return False

    def printScore(self):
        s = "Good going! You have {} apples, and ${} million in Gold!".format(self.apples, self.gold)
        print(s)
        
    def newGame(self):
        self.apples = 0
        self.gold = 0
        
    def printLoot(self):
        #this function is used for debugging
        print('apples : ', self.apples)
        print('gold   : ', self.gold)
        print('play   : ', self.play)
##       
### this ends the GameLoot class definition
##
        
def greeting():
    print("Hello and welcome!")
    print("The objective of the game is to pick apples and trade them for Gold.")
    print("You need $57 million in Gold to Win! ")
    print("Good Luck!\n")

        

def play_game(this_game):
#    print('in play_game')
    
    while this_game.playGame():
        pick = input("\nEnter 'A' to pick an apple, or 'G' to trade them for Gold -> ").upper()
        if pick == "A":
            this_game.addAnApple()
            time.sleep(.5)
            this_game.printScore() 
        elif pick == "G":
            if this_game.hasApples() == False:                
                print("Sorry, no apples to trade! Go pick some!")
            else:
                this_game.sellApples()
                this_game.printScore()
                if this_game.isAWinner():
                    print("\n * * * You Won the Game! * * *\n")
                    this_game.setPlay(input("Do you want to play again!"))
                    if this_game.playGame():
                        this_game.newGame()
                    else: print("Sorry to see you go. Bye, bye.")
                else: pass
        else:
            print("I don't understand your answer, stopping the game.\n\t Bye, bye.")
            this_game.setPlay('N')
            
#        this_game.printLoot()

def main():
    this_game = GameLoot()
    greeting()
    name = input("What's your name: ")
#    print("Hi ," + name + "\n")
#    print('after greeting')
    this_game.setPlay(input("Hi {}, are you ready to play Y/N? ".format(name)))
#    print('play game is : ', this_game.playGame())
    if this_game.playGame():
        print("Okay, lets get started...")
        play_game(this_game)
    else:
        print("Sorry to see you go. Bye, bye.")

if __name__  ==  "__main__" : main()
    
    
