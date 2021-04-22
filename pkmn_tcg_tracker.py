from card_class import PokemonCard
from gui_class import gui_class
import tkinter
from db_class import db_class


bst = db_class("BST")
#print(bst.get_set())

PC = PokemonCard('BST',bst.get_set()[157])
#print(PC.get_url())

gui_class(tkinter.Tk())