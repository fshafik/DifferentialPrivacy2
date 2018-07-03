import csv, random
import numpy as np
with open('load_halfhour.csv') as read:
	reader = csv.DictReader(read, ['halfhour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
	with open('DP-agg_0.1.csv', 'w') as write:
		writer = csv.DictWriter(write,['halfhour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
		writer.writeheader()
		read.readline()
		max_avg = 0
		max_x = [0]*11
		peak = [0.75,1,1,1.5]
		total = 0
		for row in reader:



			for i in range(len(noisy_plugs)):
				n = -1
				while n < 0:
					n = np.random.geometric(p=(0.1/569165))
					#n = np.random.normal(scale=(max_avg/0.1))
				idx = noisy_plugs[i]
				nagg += x[idx] + round(n,3)
				x[idx] += round(n,3)
				sum -= round(n,3)





			writer.writerow({ 'halfhour': row['hour'],'agg': row['agg'], 'class0': plugs[0], 'class1': plugs[1], 'class2': plugs[2], 'class3': plugs[3],
		            	'class4': plugs[4], 'class5': plugs[5],'class6': plugs[6], 'class7': plugs[7], 'class8': plugs[8],
		            	'class9': plugs[9], 'class11': plugs[10]})
print(navg*1.0/total)