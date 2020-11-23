from pprint import pprint
import json,csv

json_data = json.load(open('data.json'))

counter = 0
fields = ['Name','Affiliation','Email','No. publications','hindex','i10index','hindex5y','i10index5y','citedby','citedby5y']
with open('csv_data3.csv','w') as file:
	csvwriter = csv.writer(file)
	csvwriter.writerow(fields)
	for item in json_data:
		row = []
		row.append(item['name'])
		row.append(item['affiliation'])
		row.append(item['email'])
		row.append(len(item['publications']))
		row.append(item['hindex'])
		row.append(item['i10index'])
		row.append(item['hindex5y'])
		row.append(item['i10index5y'])
		try:
			row.append(item['citedby'])
		except:
			pass
		try:
			row.append(item['citedby5y'])
		except:
			pass
		csvwriter.writerow(row)