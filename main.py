#!/usr/bin/python

import sys
import getopt
#import alsaaudio

import alsa_hw_data
import config_generator
from pcm_holder import pcm_holder
from UI import UI

alsa_hw_data.list_cards()

interface = UI()
pcms=[]

def gen_fun():
	i=interface.query_listbox()
	if i == -1:
		interface.make_confirm_diag("No device selected! Aborting.")
		return
	dmix=interface.dmix.get()
	mult=interface.multi.get()

	default = pcm_holder("!default", "hw", "hw:"+str(i), 48000)
	pcms.append(default)
	if dmix == True:
		dmixer = pcm_holder("dmixer", "dmix", "hw:"+str(i), 48000)
		pcms.append(dmixer)
	else:
		snd = pcm_holder("snd_card", "hw", "hw:"+str(i), 48000)
		pcms.append(snd)

	config_generator.write_pcm(pcms)
	interface.make_confirm_diag("Operation completed!")

interface.make_buttons(gen_fun)
interface.make_listbox(alsa_hw_data.cards)
interface.make_checkbuttons()

interface.run_loop()
