from tkinter import *

class UI():
	def __init__(self):
		self.m = Tk()
		self.m.title('Alsa Config')

		self.frame1 = Frame(self.m, width=800, bg='white',
						   height=600)
		self.frame1.pack()
		self.list = Listbox(self.frame1)

	def run_loop(self):
		self.m.mainloop()

	def make_buttons(self, generate_cmd):
		self.gen_button = Button(self.frame1, text="Generate", command=generate_cmd, width=50, height=25)
		self.gen_button.pack()

	def make_listbox(self, data):
		#self.list = Listbox(self.frame1)

		index=0
		for card in data:
			self.list.insert(index+1, data[index])
			index=index+1

		self.list.pack()

	def query_listbox(self):
		self.items = map(int, self.list.curselection())
		l = list(self.items)
		if len(l) == 0:
			return(-1)
		index=int(l[0])
		#print("sel: "+str(index))
		return(index)

	def make_checkbuttons(self):
		self.dmix=IntVar()
		self.multi=IntVar()
		self.default=IntVar()

		self.defbt = Checkbutton(self.frame1, text="default",
									  variable=self.default)
		self.dmixbt = Checkbutton(self.frame1, text="dmix",
									  variable=self.dmix)
		self.multbt = Checkbutton(self.frame1, text="multi",
									  variable=self.multi)

		self.defbt.pack()
		self.dmixbt.pack()
		self.multbt.pack()

	def make_confirm_diag(self, msg):
		diag = Toplevel(width=30, height=20)
		diag.title("Info")

		message = Message(diag, text=msg, width=100,)
		message.pack()

		button = Button(diag, text="Okay", width=50,
							command=diag.destroy)
		button.pack()

		diag.mainloop()
