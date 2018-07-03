import csv
with open('HH0_H0.csv') as read:
     reader = csv.DictReader(read)
     with open('indv_hour.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['hour','plug','value'])
         writer.writeheader()
         with open('indv_min.csv', 'w') as write:
            writer2 = csv.DictWriter(write,fieldnames=['min','plug','value'])
            writer2.writeheader()
            x = 0;
            z = 0;
            list1 = [0]*12
            list2 = [0]*12
            if x == 0 and z == 0:
                print("yay")
            for row in reader:
                if (int(row['Timestamp']) - 1377993633)//3600 == x and row['Property'] == '0': 
                    list1[int(row['Plug'])] += float(row['Value']) 
                else:
                    for y in range(0, 12):
                        if list1[y] > 0 and y != 10:
                            writer.writerow({'hour': x, 'plug': y, 'value': list1[y]})
                    x += 1
                    list1 = [0]*12
                    if row['Property'] == '0':
                        list1[int(row['Plug'])] = float(row['Value']) 

                if (row['Property'] == '0') and ((int(row['Timestamp'])) - 1377993633)//60 == z:
                    list2[int(row['Plug'])] += float(row['Value']) 
                else:
                    for y in range(0, 12):
                        if list2[y] > 0 and y != 10:
                            writer2.writerow({'min': z, 'plug': y, 'value': list2[y]})
                    z += 1
                    list2 = [0]*12
                    if row['Property'] == '0':
                        list2[int(row['Plug'])] = float(row['Value'])

                


#, ['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1', 'agg','hourspater','class0','class1','class2','class3','class4',
 #       'class5','class6','class7','class8','class9','class11','timestamp','hoursbyone','hoursbytwo','hoursbythree','hoursbyfour','hoursbysix',
  #      'hoursbyeight','hoursbytwelve']
