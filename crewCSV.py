import json, csv

with open('normalizedCrews.json','r') as f:
	crewParsed = json.load(f)
	csvOut = open('normalizedCrew.csv','w')
	csvWriter = csv.writer(csvOut)
	count = 0
	for crewMember in crewParsed:
		if count == 0:
			header = crewMember.keys()
			csvWriter.writerow(header)
			count = count + 1
		csvWriter.writerow(crewMember.values())
csvOut.close()