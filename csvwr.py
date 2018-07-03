import csv
with open('H0.csv') as read:
     reader = csv.DictReader(read, ['ID','Timestamp','Value','Property','Plug','HH_ID','H_ID'])
     with open('HH0_H1.csv', 'w') as write:
         writer = csv.DictWriter(write,['ID','Timestamp','Value','Property','Plug','HH_ID','H_ID'])
         writer.writeheader()
         for row in reader:
             if row['HH_ID'] == '1' and row['H_ID']== '0':
                 writer.writerow(row)
