import csv
import matplotlib.pyplot as plt
from dateutil.parser import parser

fig = plt.figure()


def plot_all():
	rows = []
	output_file = 'download_speed'
	with open(output_file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			row = list(row.values())
			rows.append(row)

	p = parser()
	timeStamps = list(map(lambda x: p.parse(x[3]), rows))
	downloadSpeeds = list(map(lambda x: 0.000001 * round(float(x[6])), rows))
	print(timeStamps)
	print(downloadSpeeds)
	plt.gcf().autofmt_xdate()
	plt.plot(downloadSpeeds)
	plt.show()


if __name__ == '__main__':
	plot_all()
