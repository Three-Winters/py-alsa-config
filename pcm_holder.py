class pcm_holder():
	def __init__(self, name, atype, slave, rate, period_time, period_size, buffer_size):
		self.name = name
		self.atype = atype
		self.slave = slave
		self.rate = rate
		self.period_time = period_time
		self.period_size = period_size
		self.buffer_size = buffer_size

	def get_name(self):
		return("pcm."+self.name)

	def get_slave(self):
		return(self.slave)

	def generate_configuration(self):
		if self.atype != "dmix" and self.atype != "multi":
			return(self.get_name()+" {"+"\n"
					+"type "+self.atype+"\n"+
					   "slave.pcm \""+self.get_slave()+"\"\n"+
					   "rate "+str(self.rate)+"\n"+
					   "period_time "+str(self.period_time)+"\n"+
					   "period_size "+str(self.period_size)+"\n"+
					   "buffer_size "+str(self.buffer_size)+"\n"+
					   "}\n\n")
		if self.atype == "dmix":
			return(self.get_name()+"{\n"+
					   "type "+self.atype+"\n"+
					   "slave.pcm \""+self.get_slave()+"\"\n"+
					   "rate "+str(self.rate)+"\n"+
					   "period_time "+str(self.period_time)+"\n"+
					   "period_size "+str(self.period_size)+"\n"+
					   "buffer_size "+str(self.buffer_size)+"\n"+
					   "}\n\n")
