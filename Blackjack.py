#Let's play some blackjack!
import random

class Player(object):

	def __init__(self):
		self.__bankroll = 100
		self.__hand = []

	def checkBank(self):
		return self.__bankroll

	def checkHand(self):
		return self.__hand

class Blackjack(object):

	def __init__(self, player):
		self.deck = self.buildDeck()
		self.player = player

	def buildDeck(self):
		return [(10 if i > 10 else 'A' if i == 1 else i) for i in range(1,14) for j in range (0,4)]

	def dealCard(self):
		card = random.choice(self.deck)
		self.deck.remove(card)
		return card

	def playerInfo(self):
		print "Bankroll: " + str(self.player.checkBank())
		print "Current Hand: " + str(self.player.checkHand())


if __name__ == "__main__":
	p = Player()
	print p.checkBank()

	g = Blackjack(p)
	print g.deck

	for x in range (0,20):
		card = g.dealCard()
		if card == 'A':
			print "kjsjkndsfjnknjkdfsjnksdjnkjnkjnnjksjnkjnkjnksdf"
		print card
		print g.deck

	g.playerInfo()