import csv
with open('../H0.csv') as read:
     reader = csv.DictReader(read)
     with open('indv_hour_house.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['HH','hour','plug','value'])
         writer.writeheader()
         l, w, h = 14,14,721;
         max1 = 0
         max2 = 0
         matrix = [[[0 for x in range(l)]for y in range(w)] for z in range(h)] 
         for row in reader:
            if row['Property'] == '1':          
                time = (int(row['Timestamp']) - 1377993633)//3600
                if(time < max2):
                    max2 = time
                matrix[time+3][int(row['HH_ID'])][int(row['Plug'])] += float(row['Value'])
                #if int(row['Timestamp']) > max1:
                 #   max1 = int(row['Timestamp'])
                #if time > max2:
                 #   max2 = time

         for x in range(0,721):
            for y in range(0,14):
                for z in range(0,14):
                    if matrix[x][y][z] > 0:
                        writer.writerow({ 'HH': y,'hour': x, 'plug': z, 'value': matrix[x][y][z]})
                
         print(max1)
         print(max2)
                


#, ['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1', 'agg','hourspater','class0','class1','class2','class3','class4',
 #       'class5','class6','class7','class8','class9','class11','timestamp','hoursbyone','hoursbytwo','hoursbythree','hoursbyfour','hoursbysix',
  #      'hoursbyeight','hoursbytwelve']
#1380578399- 1377993633