import card_class
from gui_class import gui_class
import tkinter
from db_class import db_class


bst = db_class("BST")
#print(bst.get_set())

PC = card_class.PokemonCard('BST',bst.get_set()[157])
#print(PC.get_url())

gui_class(tkinter.Tk())