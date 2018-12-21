from bs4 import BeautifulSoup

import requests, json, re, time
from functlib import mainPage, castPage
apikey = 
z = 0
filename = 'imdb_tts_10000.json'

with open(filename) as f:
	
	tts = json.load(f)		
	for tt in tts:
		allDocs = []
		time.sleep(.03)

		aDoc = {}
		aDoc['tt'] = tt	
		
		payload = {'apikey' : str(apikey), 'i' : tt}
		r = requests.get('http://www.omdbapi.com/',params=payload)
		data = json.loads(r.text)
		
		with open('omdbfields.py') as ff:
			omdbFields = json.load(ff)
			for field in omdbFields:
				aDoc[field] = data.get(field, 'N/A')
		
		#set cast and crew field
		aDoc['castCrew'] = []	
		
		#Prepare IMDB castpage HTML
		castUrl = castPage(tt)
		castGet = requests.get(castUrl)
		castHtml = castGet.text
		castSoup = BeautifulSoup(castHtml, 'html.parser')
		castSect = castSoup.find_all('h4', attrs = {'class' : 'dataHeaderWithBorder'})
		
		x = 1
		for castGroup in castSect:
			groupMessy = castGroup.text
			group = " ".join(groupMessy.split())
			crewNext = castGroup.find_next_sibling('table')
			
			crewList = crewNext.find_all('td' , attrs = {'class' : 'name'})
			
			for crewMembers in crewList:
				
				crewPerson = {}
				
				crewPerson['Name'] = crewMembers.find('a').text.strip()

				crewPerson['castGroup'] = group
				crewPerson['order'] = x
				
				crewCredit = crewMembers.find_next_sibling('td', attrs = {'class' : 'credit'})
				
				if crewCredit is not None:
					crewCMessy = crewCredit.text
					crewCClean = " ".join(crewCMessy.split())
					crewPerson['Credit'] = crewCClean
				else:
					crewPerson['Credit'] = group
				aDoc['castCrew'].append(crewPerson)
				
				x = x + 1
		allDocs.append(aDoc)
		time.sleep(.03)
		json.dump(allDocs,open('allDocs_' + str(z) + '.json', 'w'), indent=2)
		print(str(z) + " out of " + "92702 completed :)")
		z = z + 1
print("All done :D")
