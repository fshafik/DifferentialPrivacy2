import csv
with open('../HH0_H0.csv') as read:
     reader = csv.DictReader(read)
     with open('load-finaldata2.csv', 'w') as write:
            writer = csv.DictWriter(write,fieldnames=['hoursbyone','hoursbysix','hoursbytwelve','timestamp','agg','class0','class1','class2',
            'class3','class4','class5','class6','class7','class8','class9','class11'])
            writer.writeheader()
            x = 1377993634
            agg = 0
            list1 = [0]*12 

            for row in reader:
                if int(row['Timestamp']) != x:
                    hour = ((x - 1377993633)//3600)
                    writer.writerow({ 'hoursbyone': hour ,'hoursbysix': hour//6,'hoursbytwelve': hour//12,'timestamp': (x), 'agg': agg, 
                    'class0': list1[0], 'class1': list1[1], 'class2': list1[2],'class3': list1[3],'class4': list1[4],'class5': list1[5],
                    'class6': list1[6],'class7': list1[7],'class8': list1[8],'class9': list1[9],'class11': list1[11]})
                    x = int(row['Timestamp'])
                    list1 = [0]*12
                    agg = 0;
                    if hour > 469 and hour < 497:
                        print ("aahhh")

                if row['Property'] == '1' and float(row['Value']) > 0: 
                    list1[int(row['Plug'])] = float(row['Value'])
                    agg += float(row['Value'])

                
                if list1[10] > 0:
                    print list1[10]
                
                
                if int(row['Timestamp']) > 1379682033 and  int(row['Timestamp']) < 1379782833:
                    print int(row['Timestamp'])
                

                