class PokemonCard():
	def __init__(self, card_set, number, name, url):
		self.card_set = card_set
		self.number = number
		self.name = name
		self.url = url
	def get_set(self):
		return self.card_set
	def get_name(self):
		return self.name
	def get_number(self):
		return self.number
	def get_url(self):
		return self.url