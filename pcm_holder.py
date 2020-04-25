
#This is a class to hold various PCM data in
#an easy to parse object.
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

	#Return the .asoundrc form of this pcm in a string.
	def generate_configuration(self):
		if self.atype != "dmix" and self.atype != "multi" and self.atype != "asym":
			return(self.get_name()+" {"+"\n"+
					"type "+self.atype+"\n"+
					   "slave.pcm \""+self.get_slave()+"\"\n"+
					   "rate "+str(self.rate)+"\n"+
					   "period_time "+str(self.period_time)+"\n"+
					   "period_size "+str(self.period_size)+"\n"+
					   "buffer_size "+str(self.buffer_size)+"\n"+
					   "}\n\n")
		if self.atype == "dmix" and self.atype != "multi":
			return(self.get_name()+"{\n"+
					   "type "+self.atype+"\n"+
					   "slave.pcm \""+self.get_slave()+"\"\n"+
					   "rate "+str(self.rate)+"\n"+
					   "period_time "+str(self.period_time)+"\n"+
					   "period_size "+str(self.period_size)+"\n"+
					   "buffer_size "+str(self.buffer_size)+"\n"+
					   "}\n\n")
		elif self.atype == "asym":

			dmix_pcm = ("pcm.demixer { \n"+
							"type dmix \nslave.pcm \"snd_card\" \nrate "+str(self.rate)+
							"\n"+"period_time "+str(self.period_time)+"\n"+
							"period_size "+str(self.period_size)+"\n"+
							"buffer_size "+str(self.buffer_size)+"\n} \n\n")

			default_pcm = (self.get_name()+" {"+"\n"
							   +"type "+self.atype+"\n"+
							   "slave.pcm \""+self.get_slave()+"\"\n"+
							   "rate "+str(self.rate)+"\n"+
							   "period_time "+str(self.period_time)+"\n"+
							   "period_size "+str(self.period_size)+"\n"+
							   "buffer_size "+str(self.buffer_size)+"\n"+
							   "}\n\n")

			out_pcm = ("pcm.out {\ntype plug \n"+
						   "slave.pcm { \ntype multi \nslaves { \n"+
						   "a {channels 2 pcm \"dmixer\" }\n"+
						   "b {channels 2 pcm \"loopout\" }\n"+
						   "}\nbindings { \n"+
						   "0 { slave a channel 0 }\n"+
						   "1 { slave a channel 1 }\n"+
						   "2 { slave b channel 0 }\n"+
						   "3 { slave b channel 1 }\n"+
						   "}\n} \nttable [\n"+
						   "[ 1 0 1 0 ] \n"+
						   "[ 0 1 0 1] \n"+
						   "] \n}\n\n")

			loopout_pcm = ("pcm.loopout { \n"+
							   "type dmix \n"+
							   "slave.pcm \"hw:Loopback,0,0\"\n"+
							   "slave { \n"+
							   "period_time "+str(self.period_time)+"\n"+
							   "period_size "+str(self.period_size)+"\n"+
							   "buffer_size "+str(self.buffer_size)+"\n"+
							   "channels 2 \n} \nbindings {\n"+
							   "0 0 \n1 1 \n} \n }\n\n")

			loopin_pcm = ("pcm.loopin { \n"+
							  "type dsnoop \n"+
							  "slave.pcm \"hw:Loopback,3,0\" \n"+
							  "slave { \nrate "+str(self.rate)+"\n"+
							  "period_time "+str(self.period_time)+"\n"+
							  "period_size "+str(self.period_size)+"\n"+
							  "buffer_size "+str(self.buffer_size)+"\n"+
							  "channels 2 \n} \nbindings { \n"+
							  "0 0 \n1 1 \n} \n}\n\n")

			return(dmix_pcm+default_pcm+out_pcm+loopout_pcm+loopin_pcm)
