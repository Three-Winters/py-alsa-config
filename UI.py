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

		self.dmixbt = Checkbutton(self.frame1, text="dmix",
									  variable=self.dmix)
		self.multbt = Checkbutton(self.frame1, text="multi (with sound loop, implies dmix)",
									  variable=self.multi)

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

	def make_spinboxes(self):
		self.rate_box = Spinbox(self.m, values=(8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 192000))
		self.p_time_box = Spinbox(self.m, values=(0, 2, 4, 8, 16, 24, 32, 64, 128))
		self.p_size_box = Spinbox(self.m, from_=0, to=65536)
		self.b_size_box = Spinbox(self.m, from_=0, to=65536)

		label1 = Label(self.m, text='Rate')
		label1.pack()
		self.rate_box.pack()

		label2 = Label(self.m, text='Period Time')
		label2.pack()
		self.p_time_box.pack()

		label3 = Label(self.m, text='Period Size')
		label3.pack()
		self.p_size_box.pack()

		label4 = Label(self.m, text='Buffer Size')
		label4.pack()
		self.b_size_box.pack()
