from tkinter import *
import urllib.request
#type in card name
#displays imgage of card from url

class gui_class():
	def addchat(self):
		self.card_input_text = self.nameEntered.get()
		self.processInput()
		self.nameEntered.delete(0,END) # deletes your textbox text

	def processInput(self):
		self.temp = self.card_input_text
		print(self.temp)

	
		

	def __init__(self,form):
		
		tk = form
		#main window creation
		tk.title("Pokemon GUI")
		#tk.configure(width=500, height=300)
		tk.geometry('300x400')
		tk.configure(bg='lightgray')


		frame = Frame(tk)
		frame.configure(width = 500, height = 300) 
		frame.pack(side = TOP)

	
		form.bind("<Return>", lambda x: self.addchat())
		#textbox input
		name = ""
		self.nameEntered = Entry(frame, width = 15, textvariable = name)
		self.nameEntered.pack(side = TOP)
		
		img = PhotoImage(file = 'CardImage')
		canvas = Canvas(width = 300, height = 400)
		canvas.pack()
		canvas.create_image(20,20, anchor=NW, image=img)
		frame.pack(side = TOP)

		tk.mainloop()