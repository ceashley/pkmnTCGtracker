class PokemonCard():
	def __init__(self, card_set, card):
		self.card_set = card_set
		self.card = card
			
	def get_set(self):
		return self.card_set
	def get_card(self):
		return self.card

	def get_url(self):
		#creates the url for the image of pokemons
		url = 'http://images.pokegoldfish.com/images/gf/'
		temp_list = (self.card.split(" ", 1))
		name = temp_list[1].replace(' ','-')
		card_number = temp_list[0]
		#name is the card name with dash for spaces
		#card number is the cards number
		url+=name+'-'+self.card_set+'-'+card_number+'.jpg'
		return(url)