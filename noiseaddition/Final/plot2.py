import csv, random
import numpy as np
from matplotlib import pyplot as plt
with open('DP-load_halfhour_10.csv') as read:
	reader = csv.DictReader(read, ['halfhour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
	reader.next()
	time1 = []
	readings1 = []
	readings2 = []
	for row in reader:
		#if int(row['halfhour']) > 940 and int(row['halfhour']) < 1000:
			readings1 = np.append(readings1, [float(row['class3'])])
			#readings2 = np.append(readings2, [float(row['class1'])])
			time1 = np.append(time1, [int(row['halfhour'])])

with open('DP-load_halfhour_1.csv') as read:
	reader = csv.DictReader(read, ['halfhour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
	reader.next()
	time2 = []
	#readings1 = []
	readings2 = []
	for row in reader:
		if int(row['halfhour']) > 1292 and int(row['halfhour']) < 1345:
			readings2 = np.append(readings2, [float(row['class0'])])
			#readings2 = np.append(readings2, [float(row['class1'])])
			time2 = np.append(time2, [int(row['halfhour'])])

with open('load_halfhour.csv') as read:
	reader = csv.DictReader(read, ['halfhour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
	reader.next()
	time3 = []
	#readings1 = []
	readings3 = []
	for row in reader:
		if int(row['halfhour']) > 1240 and int(row['halfhour']) < 1290:
			readings3 = np.append(readings3, [float(row['class0'])])
			#readings2 = np.append(readings2, [float(row['class1'])])
			time3 = np.append(time3, [int(row['halfhour'])])
	
print(readings1)
print(readings3)	

#plt.plot(time1,readings1)
plt.plot(time2,readings2)
print (np.mean(readings2))
print (np.mean(readings3))
#plt.plot(time3,readings3)

plt.show()


#DP-agg_halfhour_geo.csv
#agg_halfhour.csv
#DP-thirtymin.csv
