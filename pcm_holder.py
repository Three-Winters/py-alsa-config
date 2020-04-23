class pcm_holder():
	def __init__(self, name, atype, slave, rate):
		self.name = name
		self.atype = atype
		self.slave = slave
		self.rate = rate

	def get_name(self):
		return("pcm."+self.name)

	def get_slave(self):
		return(self.slave)

	def generate_configuration(self):
		return(self.get_name()+" {"+"\n"
				   +"type "+self.atype+"\n"
				   +"slave.pcm \""+self.get_slave()
				   +"\"\n"+"}")
