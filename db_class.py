PATH = "card_database/"
EXTENSION = ".pkmndb.parsed"
class db_class():
	def __init__(self, pkmn_set):
		self.pkmn_set = pkmn_set
	def get_set(self):
		dbfile = open(PATH + self.pkmn_set + EXTENSION, "r")
		db = []
		for line in dbfile:
			db.append(line.strip('\n'))
		return db
	