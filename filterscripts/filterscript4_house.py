import csv
with open('../H0.csv') as read:
     reader = csv.DictReader(read)
     with open('housedata.csv', 'w') as write:
            writer = csv.DictWriter(write,fieldnames=['hoursbyone','hoursbysix','hoursbytwelve','HH','timestamp','agg','class0','class1','class2',
            'class3','class4','class5','class6','class7','class8','class9','class10','class11','class12','class13'])
            writer.writeheader()
            x = 1377993634
            agg = 0
            list1 = [0]*14
            max = 0;
            HH = 0;

            for row in reader:
                print("timestamp:" ,(int(row['Timestamp']))," ", (int(row['Timestamp']) != x))
                print("house:", (int(row['HH_ID'])), " ", (int(row['HH_ID']) != HH))
                if (int(row['Timestamp']) != x) | (int(row['HH_ID']) != HH):
                    hour = ((x - 1377993633)//3600)
                    writer.writerow({ 'hoursbyone': hour ,'hoursbysix': hour//6,'hoursbytwelve': hour//12,'HH': HH,'timestamp': (x), 'agg': agg, 
                    'class0': list1[0], 'class1': list1[1], 'class2': list1[2],'class3': list1[3],'class4': list1[4],'class5': list1[5],
                    'class6': list1[6],'class7': list1[7],'class8': list1[8],'class9': list1[9],'class10': list1[10], 'class11': list1[11], 
                    'class12': list1[12],'class13': list1[13]})
                    x = int(row['Timestamp'])
                    HH = int(row['HH_ID'])
                    list1 = [0]*14
                    agg = 0;                    

                if row['Property'] == '1' and float(row['Value']) > 0: 
                    #print(int(row['Plug']))
                    list1[int(row['Plug'])] |= 1
                    agg += float(row['Value'])
                
                

                


#, ['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1', 'agg','hourspater','class0','class1','class2','class3','class4',
 #       'class5','class6','class7','class8','class9','class11','timestamp','hoursbyone','hoursbytwo','hoursbythree','hoursbyfour','hoursbysix',
  #      'hoursbyeight','hoursbytwelve']
