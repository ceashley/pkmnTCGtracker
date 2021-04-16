import card_class
from db_class import db_class

bst = db_class("BST")
#print(bst.get_set())

PC = card_class.PokemonCard('BST',bst.get_set()[157])
#print(PC.get_url())

