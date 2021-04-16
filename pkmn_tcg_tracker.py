import card_class
from tkinter import *
from gui import gui

root = Tk()
gui.main_gui(root)

#pokemon object: card set, number, name, url
bellsprout = card_class.PokemonCard("battleStyles", 1, "bellsprout", "url")

print(bellsprout.get_set())
print(bellsprout.get_number())
print(bellsprout.get_name())
print(bellsprout.get_url())