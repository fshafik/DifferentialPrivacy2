import csv
with open('housedata.csv') as read:
     reader = csv.DictReader(read)
     with open('agg_hour_house2.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['HH','hour','agg','class0','class1','class2','class3','class4','class5','class6','class7','class8','class9',
            'class10', 'class11', 'class12', 'class13'])
         writer.writeheader()
         i = reader.next();
         x = (int(i['timestamp']) - 1377993633)//3600;
         agg = [0]*14;
         HH = 0;
         h = [[0 for i in range(14)] for j in range(14)]
         for row in reader:
            if (int(row['timestamp']) - 1377993633)//3600 == x:
                agg[(int(row['HH']))] += float(row['agg'])
                #h[(int(row['HH']))][0] |= int(float(row['class0']))
                #h[(int(row['HH']))][1] |= int(float(row['class1']))
                #h[(int(row['HH']))][2] |= int(float(row['class2']))
                #h[(int(row['HH']))][3] |= int(float(row['class3'])) 
                #h[(int(row['HH']))][4] |= int(float(row['class4']))
                #h[(int(row['HH']))][5] |= int(float(row['class5']))                   
                #h[(int(row['HH']))][6] |= int(float(row['class6']))
                #h[(int(row['HH']))][7] |= int(float(row['class7']))
                #h[(int(row['HH']))][8] |= int(float(row['class8']))
                #h[(int(row['HH']))][9] |= int(float(row['class9'])) 
                #h[(int(row['HH']))][10] |= int(float(row['class10'])) 
                #h[(int(row['HH']))][11] |= int(float(row['class11']))
                #h[(int(row['HH']))][12] |= int(float(row['class12'])) 
                #h[(int(row['HH']))][13] |= int(float(row['class13']))
                h[(int(row['HH']))][0] = int(float(row['class0']))
                h[(int(row['HH']))][1] = int(float(row['class1']))
                h[(int(row['HH']))][2] = int(float(row['class2']))
                h[(int(row['HH']))][3] = int(float(row['class3'])) 
                h[(int(row['HH']))][4] = int(float(row['class4']))
                h[(int(row['HH']))][5] = int(float(row['class5']))                   
                h[(int(row['HH']))][6] = int(float(row['class6']))
                h[(int(row['HH']))][7] = int(float(row['class7']))
                h[(int(row['HH']))][8] = int(float(row['class8']))
                h[(int(row['HH']))][9] = int(float(row['class9'])) 
                h[(int(row['HH']))][10] = int(float(row['class10'])) 
                h[(int(row['HH']))][11] = int(float(row['class11']))
                h[(int(row['HH']))][12] = int(float(row['class12'])) 
                h[(int(row['HH']))][13] = int(float(row['class13']))
            else:
                for y in range(14):
                    writer.writerow({'HH': y,'hour': x, 'agg': agg[y], 'class0': h[y][0], 'class1': h[y][1],'class2': h[y][2], 'class3': h[y][3],
                        'class4': h[y][4], 'class5': h[y][5],'class6': h[y][6], 'class7': h[y][7], 'class8': h[y][8],'class9': h[y][9],'class10': h[y][10], 
                        'class11': h[y][11], 'class12': h[y][12], 'class13': h[y][13]})
                    h[y] = [0]*14

                agg = [0]*14
                agg[(int(row['HH']))] = float(row['agg'])
                x = (int(row['timestamp']) - 1377993633)//3600
                h[(int(row['HH']))][0] = int(float(row['class0']))
                h[(int(row['HH']))][1] = int(float(row['class1']))
                h[(int(row['HH']))][2] = int(float(row['class2']))
                h[(int(row['HH']))][3] = int(float(row['class3'])) 
                h[(int(row['HH']))][4] = int(float(row['class4']))
                h[(int(row['HH']))][5] = int(float(row['class5']))                   
                h[(int(row['HH']))][6] = int(float(row['class6']))
                h[(int(row['HH']))][7] = int(float(row['class7']))
                h[(int(row['HH']))][8] = int(float(row['class8']))
                h[(int(row['HH']))][9] = int(float(row['class9'])) 
                h[(int(row['HH']))][10] = int(float(row['class10'])) 
                h[(int(row['HH']))][11] = int(float(row['class11']))
                h[(int(row['HH']))][12] = int(float(row['class12'])) 
                h[(int(row['HH']))][13] = int(float(row['class13']))

