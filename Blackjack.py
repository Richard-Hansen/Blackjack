#Let's play some blackjack!
import random

class Player(object):

	def __init__(self):
		self.__bankroll = 100

	def checkBank(self):
		return self.__bankroll

class Game(object):

	def __init__(self):
		self.deck = self.buildDeck()

	def buildDeck(self):
		return [(10 if i > 10 else i) for i in range(1,14) for j in range (0,4)]


if __name__ == "__main__":
	p = Player()
	print p.checkBank()

	g = Game()
	print g.deck
