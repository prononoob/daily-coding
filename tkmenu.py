from tkinter import *
from tkinter import ttk


class App:
	def __init__(self):
		self.root = Tk()
		self.frm = ttk.Frame(self.root, padding=10)
		self.frm.pack()
		self.comms = Commands()
		ttk.Label(self.frm, text='Hello World!').pack()
		
	def buttonSetup(self):
		self.buttonCounter = 1
		self.button1 = ButtonBuilder('bruh', command=self.comms.retbruh)
		self.button2 = ButtonBuilder('Testuje')
		self.button3 = ButtonBuilder('czy dziala')
		ttk.Entry(self.frm, width=10).pack()
		ttk.Button(self.frm, text='Quit', command=self.root.destroy).pack()
		self.root.geometry('300x300')
		self.root.mainloop()

class ButtonBuilder:
	def __init__(self, text, command=None):
		self.text, self.command = text, command
		self.butt = ttk.Button(myapp.frm, text=self.text, command=self.command)
		self.butt.pack()

class Commands:
	def retbruh(self):
		print('bruh')


'''class App:
	def __init__(self):
		self.root = Tk()
		self.frm = ttk.Frame(self.root, padding=10)
		self.frm.grid()
		ttk.Label(self.frm, text='Hello World!').grid(column=0, row=0)
		
	def buttonSetup(self):
		self.buttonCounter = 1
		self.button1 = ButtonBuilder('bruh')
		self.button2 = ButtonBuilder('Testuje')
		self.button3 = ButtonBuilder('czy dziala')
		self.buttonCounter += 1
		ttk.Entry(self.root, width=20).grid(column=0, row=self.buttonCounter)
		ttk.Button(self.frm, text='Quit', command=self.root.destroy).grid(column=0, row=self.buttonCounter+1)
		#self.root.geometry('300x300')
		self.root.mainloop()

class ButtonBuilder:
	def __init__(self, text):
		self.text = text
		self.butt = ttk.Button(myapp.frm, text=self.text).grid(column=0, row=myapp.buttonCounter)
		myapp.buttonCounter += 1'''


myapp = App()
myapp.buttonSetup()
