import csv
with open('../../individual plugs/indv_min2.csv') as read:
     reader = csv.DictReader(read)
     with open('load_min_i.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['min','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
         writer.writeheader()
         i = reader.next()
         x = 0
         plugs = [0]*12
         agg = 0;
         for row in reader:
         	if int(row['min']) != x:
         		writer.writerow({ 'min': x,'agg': agg, 'class0': plugs[0], 'class1': plugs[1], 'class2': plugs[2], 'class3': plugs[3],
		            	'class4': plugs[4], 'class5': plugs[5],'class6': plugs[6], 'class7': plugs[7], 'class8': plugs[8],
		            	'class9': plugs[9], 'class11': plugs[11]})
         		agg = 0
         		plugs = [0]*12
         		x =  int(row['min'])

         	agg += float(row['value'])
         	plugs[int(row['plug'])] = float(row['value'])

