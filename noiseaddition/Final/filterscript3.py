import csv
with open('DP-load_hour_10.csv') as read:
     reader = csv.DictReader(read)
     with open('DP-indv_hour_10.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['hour','plug','value'])
         writer.writeheader()

         for row in reader:
            for i in range(10):
                x = 'class' + str(i)
                if(float(row[x]) > 0):
                    writer.writerow({'hour': int(row['hour']), 'plug': i, 'value': row[x]})

            writer.writerow({'hour': int(row['hour']), 'plug': 11, 'value': row['class11']})
                

                


#, ['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1', 'agg','hourspater','class0','class1','class2','class3','class4',
 #       'class5','class6','class7','class8','class9','class11','timestamp','hoursbyone','hoursbytwo','hoursbythree','hoursbyfour','hoursbysix',
  #      'hoursbyeight','hoursbytwelve']
#1380578399- 1377993633