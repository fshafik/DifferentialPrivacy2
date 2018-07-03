import csv
with open('loaddata.csv') as read:
     reader = csv.DictReader(read)
     with open('load_hour.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['hour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9','class11'])
         writer.writeheader()
         i = reader.next()
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
            #if (int(row['tenmin']))//3 == x:
                agg += (float(row['class0'])) + (float(row['class1'])) + (float(row['class2'])) + (float(row['class3'])) + (float(row['class4'])) + (float(row['class5'])) + (float(row['class6'])) + (float(row['class7'])) + (float(row['class8'])) + (float(row['class9'])) + (float(row['class11'])) 

                class0 += (float(row['class0']))
                class1 += (float(row['class1']))
                class2 += (float(row['class2']))
                class3 += (float(row['class3'])) 
                class4 += (float(row['class4']))
                class5 += (float(row['class5']))
                class6 += (float(row['class6'])) 
                class7 += (float(row['class7']))
                class8 += (float(row['class8']))
                class9 += (float(row['class9'])) 
                class11 += (float(row['class11']))  
            else:
                writer.writerow({'hour': x, 'agg': agg, 'class0': class0, 'class1': class1, 'class2': class2, 'class3': class3,
                    'class4': class4, 'class5': class5,'class6': class6, 'class7': class7, 'class8': class8,
                    'class9': class9, 'class11': class11 })
                agg = (float(row['class0'])) + (float(row['class1'])) + (float(row['class2'])) + (float(row['class3'])) + (float(row['class4'])) + (float(row['class5'])) + (float(row['class6'])) + (float(row['class7'])) + (float(row['class8'])) + (float(row['class9'])) + (float(row['class11'])) 

                x = (int(row['timestamp']) - 1377993633)//3600
            #    x = (int(row['tenmin']))//3
                class0 = (float(row['class0']))
                class1 = (float(row['class1']))
                class2 = (float(row['class2']))
                class3 = (float(row['class3'])) 
                class4 = (float(row['class4']))
                class5 = (float(row['class5']))
                class6 = (float(row['class6'])) 
                class7 = (float(row['class7']))
                class8 = (float(row['class8']))
                class9 = (float(row['class9'])) 
                class11 = (float(row['class11']))  