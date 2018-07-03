import csv, random
import numpy as np
with open('load_hour_i.csv') as read:
	reader = csv.DictReader(read, ['hour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
	with open('DP-load_hour_10.csv', 'w') as write:
		writer = csv.DictWriter(write,['hour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
		writer.writeheader()
		read.readline()
		max_avg = 0
		max_x = [0]*11
		navg = 0
		total = 0
		for row in reader:
			x = []
			w = []
			z = []
			y = 0
			avg = 0
			nagg = 0
			#loop to set average of row, number of on plugs, as well as which plugs are on and which are off
			for i in range(11):
			    if i != 10:
			    	x = np.append(x,[float(row['class' + str(i)])])
			    else:
			    	x = np.append(x,[float(row['class11'])])
			    avg += x[i]
			    total += 1
		            if x[i] == 0:
			    	z = np.append(z, [int(i)])
			    else:
			    	y += 1
			    	if x[i] < (max_avg):
			    		w = np.append(w, [int(i)])
			    		navg += 1

			oldx = list(x)
			if(float(row['agg']) <= 0):
				noisy_plugs = [0]*11
			else:
				#setting average to be used later in noise generation
				avg = avg/y if y > 0 else 0
				max_x = list(x) if avg > max_avg else list(max_x)
				max_avg = avg if avg > max_avg else max_avg
				print('MAX AVG ', max_avg)
				print('MAX X ', max_x)
				#first pass to decide how many and which OFF plugs are to be ON
				noisy_plugs = []
				noisy_plugs = np.array(noisy_plugs, dtype = int)
	 			population = [0,1]
				weights = [0.51,0.49] #decided according to the epsilon of randomized response

				for i in range(len(z)):
					dec = np.random.choice(population, p=weights)
					noisy_plugs = np.append(noisy_plugs,int(z[i]))

				#handle 0 noise case
				noise = len(noisy_plugs)
				if 1 == 0:
					noisy_plugs = [0]*11
				else:
					#second pass to generate sum
					sum = 0
					per = 1.0/(y + noise) #percentage of value to be taken from ON plugs to be redistributed
					#print "xfore " + str(x)

					for i in range(11):
						rem = per*x[i]
						x[i] -= round(rem,3)
						x[i] = round(x[i],3)
						sum += round(rem,3)

					#third pass to add noise to both noisy and ON plugs, and alter the sum accordingly
					save_sum = sum
					w = np.array(w, dtype = int)
					noisy_plugs = np.append(noisy_plugs, w) #these are all the plugs which will have noise added to them
					

					for i in range(len(noisy_plugs)):
						n = -1
						while n < 0:
							n = np.random.geometric(p=(10/max_avg))
						#n = np.random.normal(scale=(max_avg/0.1))
						idx = noisy_plugs[i]
						nagg += x[idx] + round(n,3)
						x[idx] += round(n,3)
						sum -= round(n,3)

					#print "xnoise " + str(x)
					
					#fourth pass to redistribute the rest of the sum on noisy and ON plugs - smoothie
					save_sum = sum
					for i in range(len(noisy_plugs)):
						idx = noisy_plugs[i]
						sub = round(((x[idx]*1.0)/nagg)*save_sum,3)
						x[idx] += sub
						x[idx] = round(x[idx],3)
						sum -= sub

					#print "xsmooth " + str(x)

			plugs = x
			#print float(row['agg'])
			#if int(row['halfhour']) > 500 and int(row['halfhour']) < 1100:
			print 'plugs ', str(plugs)
			print 'oldx ', str(oldx)

			writer.writerow({ 'hour': row['hour'],'agg': row['agg'], 'class0': plugs[0], 'class1': plugs[1], 'class2': plugs[2], 'class3': plugs[3],
		            	'class4': plugs[4], 'class5': plugs[5],'class6': plugs[6], 'class7': plugs[7], 'class8': plugs[8],
		            	'class9': plugs[9], 'class11': plugs[10]})
print(navg*1.0/total)