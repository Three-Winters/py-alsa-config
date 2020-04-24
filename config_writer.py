
#This function writes our desired pcms to the .asoundrc
def write_pcm(pcm_data):
	with open('.asoundrc', 'w') as f:
		for pcm in pcm_data:
			f.write(pcm.generate_configuration())
