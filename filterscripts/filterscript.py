import csv
with open('../noiseaddition/DP-finaldata2.csv') as read:
     reader = csv.DictReader(read)
     with open('DP-agg_hour_mn.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['hour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
         writer.writeheader()
         i = reader.next();
         x = (int(i['timestamp']) - 1377993633)//3600
         agg = 0;
         class0 = 0 
         class1 = 0
         class2 = 0
         class3 = 0
         class4 = 0
         class5 = 0
         class6 = 0
         class7 = 0
         class8 = 0
         class9 = 0
         class11 = 0
         for row in reader:
            if (int(row['timestamp']) - 1377993633)//3600 == x:
                agg += float(row['agg'])
                class0 |= int(float(row['class0']))
                class1 |= int(float(row['class1']))
                class2 |= int(float(row['class2']))
                class3 |= int(float(row['class3'])) 
                class4 |= int(float(row['class4']))
                class5 |= int(float(row['class5']))
                class6 |= int(float(row['class6'])) 
                class7 |= int(float(row['class7']))
                class8 |= int(float(row['class8']))
                class9 |= int(float(row['class9'])) 
                class11 |= int(float(row['class11']))  
            else:
                writer.writerow({'hour': x, 'agg': agg, 'class0': class0, 'class1': class1, 'class2': class2, 'class3': class3,
                    'class4': class4, 'class5': class5,'class6': class6, 'class7': class7, 'class8': class8,
                    'class9': class9, 'class11': class11 })
                agg = float(row['agg'])
                x = (int(row['timestamp']) - 1377993633)//3600
                class0 = int(float(row['class0']))
                class1 = int(float(row['class1']))
                class2 = int(float(row['class2']))
                class3 = int(float(row['class3'])) 
                class4 = int(float(row['class4']))
                class5 = int(float(row['class5']))
                class6 = int(float(row['class6'])) 
                class7 = int(float(row['class7']))
                class8 = int(float(row['class8']))
                class9 = int(float(row['class9'])) 
                class11 = int(float(row['class11']))  