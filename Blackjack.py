#Let's play some blackjack!
import random

class Player(object):

	def __init__(self, isDealer):
		self.isDealer = isDealer
		self.bankroll = 100
		self.hand = []

	def checkBank(self):
		return self.bankroll

	def checkHand(self):
		return self.hand


class Blackjack(object):

	def __init__(self, player, dealer):
		self.deck = self.buildDeck()
		self.player = player
		self.dealer = dealer;

	def buildDeck(self):
		return [(10 if i > 10 else 'A' if i == 1 else i) for i in range(1,14) for j in range (0,4)]

	def dealCard(self, person):
		card = random.choice(self.deck)
		person.hand.append(str(card))# adds card to paramater "player"'s hand

		if (not person.isDealer):
			print "You received: " + str(card)

		if (len(person.hand) > 1):
			if (not person.isDealer):
				print "Your current hand is: " + str(self.player.checkHand())
			elif (len(person.hand) < 3):
				print "The dealer's is showing: " + str(self.dealer.checkHand()[0])
			else:
				print "The dealer's hand is: " + str(self.dealer.checkHand())

		self.deck.remove(card)
		return card

	def makeBet(self):
		print "Please enter your bet!"
		while True:
			try:
				bet = int(raw_input())
			except:
				print "You did not enter an integer!"
				continue
			else:
				if (bet > self.player.checkBank()):
					print "You only have $" + str(self.player.checkBank()) + "! Try a smaller bet!"
				elif (bet < 0):
					print "Nice try! You can't make a negative bet!"
				else:
					self.bet = bet
					self.player.bankroll = self.player.bankroll - bet
					print "Your bet has been placed at: " + str(self.bet)
					break

	def sumCardsLow(self, person):
		sumCards = 0

		for x in person.hand:
			if x == 'A':
				sumCards += 1
			else:
				sumCards += int(x)

		return sumCards

	def sumCardsHigh(self, person):
		sumCards = 0

		for x in person.hand:
			if x == 'A':
				sumCards += 11
			else:
				sumCards += int(x)

		return sumCards

	def bestHand(self, person):
		lower = self.sumCardsLow(person)
		higher = self.sumCardsHigh(person)

		if (higher > lower and higher < 22):
			return higher
		return lower

	def runDealer(self):
		while (self.bestHand(self.dealer) < 16):
			self.dealCard(self.dealer)

	def resetHands(self):
		self.player.hand = []
		self.dealer.hand = []
		self.deck = self.buildDeck()


def playGame(b):
	print "Welcome to Blackjack! Let's get started!"

	while True:
		playerScore = 0
		dealerScore = 0

		b.makeBet()
		b.dealCard(b.player)
		b.dealCard(b.player)
		playerScore = b.bestHand(b.player)

		b.dealCard(b.dealer)
		b.dealCard(b.dealer)
		dealerScore = b.bestHand(b.dealer)

		while True:
			choice = raw_input("Hit (h) or stay (s)?")

			if choice == "h":
				b.dealCard(b.player)
				playerScore = b.bestHand(player)
				if (playerScore > 21):
					print "You Bust!"
					break
			elif choice == "s":
				b.runDealer()
				dealerScore = b.bestHand(b.dealer)
				break;
			else:
				print "Invalid choice"
				continue

		if (playerScore > 21):
			print "The dealer won! You lost: " + str(b.bet)
		elif (dealerScore > 21 or playerScore > dealerScore):
			b.player.bankroll += (2 * b.bet)
			print "You won $" + str(b.bet * 2) + "!"
		elif (dealerScore == playerScore):
			b.player.bankroll += b.bet
			print "Push! You get your bet of: $" + str(b.bet) + " back!"
		else:
			print "The dealer won! You lost: $" + str(b.bet)

		choice = raw_input("Would you like to play again? (y) (n)")

		if (choice is not "y"):
			break
		else:
			b.resetHands()


if __name__ == "__main__":
	player = Player(False)
	dealer = Player(True)
	blackjack = Blackjack(player, dealer)
	playGame(blackjack)

	