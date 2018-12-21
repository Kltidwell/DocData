import json

x = 0
combineData = []

while x <= 92697:
	with open('allDocs_'+str(x)+'.json','r') as f:
		docFile = json.load(f)
		
		for doc in docFile:
			combineData.append(doc)
		print('Adding ' + str(x) + ' of 92697')
		x = x + 1
	
json.dump(combineData, open('combineData.json', 'w'), indent=2)
	