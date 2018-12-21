import json

normalizedCrews = []
x = 0
with open('castcrewGender.json', 'r') as f:
	movies = json.load(f)
	for movie in movies:
		for person in movie['castCrew']:
			crewPerson = {}
			crewPerson['tt'] = movie['tt']
			crewPerson['Title'] = movie['Title']
			crewPerson['Year'] = movie['Year']
			crewPerson['tableauyear'] = '01/01/'+str(movie['Year'])
			crewPerson['Names'] = person['Name']
			crewPerson['castGroup'] = person['castGroup']
			crewPerson['order'] = person['order']
			crewPerson['Credit'] = person['Credit']
			crewPerson['guessedGender'] = person['guessedGender']
			
			normalizedCrews.append(crewPerson)
		x = x + 1
		print('normalized ' + str(x) + ' of ' + str(len(movies)))
json.dump(normalizedCrews, open('normalizedCrews.json', 'w'), indent=2)
print('All done :)')
		
