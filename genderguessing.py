import json, re
import gender_guesser.detector as gender
d = gender.Detector()
x = 0

#regex for first name
expr = re.compile('(\w*)')
dataGender = []

with open('combineData.json','r') as f:
	movies = json.load(f)
	for movie in movies:
		for person in movie['castCrew']:
			strResults = expr.search(person['Name'])
			person['guessedGender'] = d.get_gender(strResults.group())
		dataGender.append(movie)
		print('Done with ' + str(x) + ' of ' + str(len(movies)))
		x = x + 1
json.dump(dataGender, open('castcrewGender.json','w'), indent = 2)
