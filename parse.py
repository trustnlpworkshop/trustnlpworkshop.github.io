import csv
data = []
with open("papers.tsv") as fd:
	rd = csv.reader(fd,delimiter="\t")
	for row in rd:
		data.append(row)

for row in data[1:]:
	items= row
	print('<li><a href="papers/%s.pdf">%s</a>, %s </li>' %(items[0], items[1], items[5]))
