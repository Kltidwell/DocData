from bs4 import BeautifulSoup

import requests, json
from datetime import date
from functlib import numAllresults, numberResults

x = 1878

amtperYear = []
endDate = date(1, 1, 1)

while endDate <= date(2016, 12, 31):
	
	startDate = date(x, 1, 1)
	endDate = date(x, 12, 31)

	year = {}
	year['year'] = x
	year['yearTableau'] = '01/01/' + str(x)
	numAll = numAllresults(startDate, endDate)
	numDoc = numberResults(startDate, endDate)
	year['amtAll'] = numAll
	year['amtDoc'] = numDoc
	year['amtminusDoc'] = numAll-numDoc
	amtperYear.append(year)
	print('Looking at ' + str(x))
	x = x + 1
	
	
json.dump(amtperYear,open('amtperYear_02.json','w'),indent=2)
