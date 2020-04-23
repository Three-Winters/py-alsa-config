import alsaaudio

cards = {}

def list_cards():
	cards.clear()
	count = 0
	for i in alsaaudio.card_indexes():
		(name, longname) = alsaaudio.card_name(i)
		cards[count] = longname
		count = count+1
