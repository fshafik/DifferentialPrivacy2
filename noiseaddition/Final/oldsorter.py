import sys, csv ,operator
with open('load-finaldata.csv') as read:
    data = csv.DictReader(read)
    with open("loaddata.csv", "w") as f:
    	sortedlist = sorted(data, key=operator.itemgetter('timestamp'))
    	fileWriter = csv.DictWriter(f,fieldnames=['hoursbyone','hoursbysix','hoursbytwelve','HH','timestamp','agg','class0','class1','class2',
            'class3','class4','class5','class6','class7','class8','class9','class11'])
    	fileWriter.writeheader()
	for row in sortedlist:
	    fileWriter.writerow(row)
