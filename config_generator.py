
def write_pcm(pcm_data):
	with open('test-asoundrc', 'w') as f:
		for pcm in pcm_data:
			#f.write(format_data(pcm))
			f.write(pcm.generate_configuration())
