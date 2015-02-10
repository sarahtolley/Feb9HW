from __future__ import division

import re

#list accession names
accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

#write for loop
for acc in accs:
	#print only accession names containing the number 5
	if re.search(r"5", acc):
		print("Containing 5: " +"\t" + acc)

#contain the letter d or e
for acc in accs:
	if re.search(r"(d|e)", acc):
			print("d or e: " + "\t" + acc)

#contain the letters d and e in that order
for acc in accs:
	if re.search(r"d.*e", acc):
		print("d and e in that order: " + "\t" + acc)

#contain the letters d and e in that order with a single letter between them
for acc in accs:
	if re.search(r"d.e", acc):
		print("d and e in that order with letter: " + "\t" + acc)
