#Let's play some blackjack!

class Player(object):

	def __init__(self):
		self.__bankroll = 100

	def checkBank(self):
		return self.__bankroll

if __name__ == "__main__":
	p = Player()
	print p.checkBank()
