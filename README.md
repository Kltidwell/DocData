#American Documentaries, 1878 to 2017

The goal of this project is to use data from IMDB to compare the growth of documentary versus non-documentary movies made in the United States from 1878 to 2017 and to compare the gender breakdown of different jobs on documentary crews. Currently, the initial data has been gathered to do the analysis but further cleaning and normalizing is necessary before it can be used for visualization or analysis.


This project contains the following:

functlib.py

-----A function library used by many of the following programs.
	
omdbfields.py

-----An edited list of OMDB fields for use in getdata_00.py.


**webscraping codes**

Get_with_range.py

-----Allows scraping IMDB ids in the advanced search results of IMDB, even when results are over 10,000 items, which can result in 404s or unusual urls. Checks date ranges, adjusts dates for fewer than 10,000 results, scrapes those results, the checks the next range.

getdata_00.py
	
-----Takes a list of tt numbers and combines movie metadata from OMDb with scraped resutls from IMDB cast and crew pages.

getallmovieamounts.py

-----Gets the number of documentaries and non-documentaries listed in IMDB from a date range.
	
**data editing**

combine.py

-----combines the results of getdata_00.py into one document.
	
genderguessing

-----Takes the results of the combined documents and guesses the gender of each crew person.

normalizeCrew.py

-----Normalizes the crew members from the combined document.

crewCSV.py
	
-----Doesn't work....yet. Runs into bad characters when turning the combiend datset into a csv.

**data sets**

amtperYear.py

-----Number of American documentaries, non-documentaries, and both per year from 1878 to 2017 

imdb_tts_10000.json

-----IMDB unique ids of all American documentaries from 1878 to 2017.

combineData.json

-----Data for each documentary in imdb_tts_10000.json.
	
-----Example record:
	
-----{
 
-----"tt": "tt2221420",
 
-----"Title": "Sallie Gardner at a Gallop",
 
-----"Year": "1878",
 
-----"Released": "15 Jun 1878",
 
-----"Runtime": "1 min",
 
-----"Genre": "Short",
 
-----"Plot": "The clip shows a jockey, Domm, riding a horse, Sally Gardner. The clip is not filmed but instead consists of 24 individual photographs shot in rapid succession, making a moving picture when using a zoopraxiscope.",
 
-----"Language": "None",
 
-----"Country": "USA",

-----"Awards": "N/A",
 
-----"Ratings": [

	
-----{

-----"Source": "Internet Movie Database",

-----"Value": "7.4/10"

-----}

-----],

-----"Type": "movie",

-----"BoxOffice": "N/A",

-----"Production": "N/A",

-----"castCrew": [

-----{

-----"Name": "Eadweard Muybridge",

-----"castGroup": "Directed by",

-----"order": 1,

-----"Credit": "Directed by"

		},

----- {

	  "Name": "Leland Stanford",

-----"castGroup": "Produced by",

-----"order": 2,

-----"Credit": "producer"

		},

----- {

	  "Name": "Eadweard Muybridge",

-----"castGroup": "Cinematography by",

-----"order": 3,
----- 
	  "Credit": "Cinematography by"
----- 
	  }
	
castcrewGender.json

-----Same as the above but with guessed gender for each crew person absed on the data from david.arcos' gender-guesser.

-----Example castCrew section:

-----"castCrew": [

-----{

-----"Name": "Brian Ekdale",

-----"castGroup": "Directed by",

-----"order": 1,

-----"Credit": "Directed by",

-----"guessedGender": "male"

-----},

-----{

-----"Name": "Gary Burns",

-----"castGroup": "Produced by",

-----"order": 2,

-----"Credit": "associate producer",

-----"guessedGender": "male"

-----},

----- {

-----"Name": "Lois Self",

-----"castGroup": "Produced by",

-----"order": 3,

-----"Credit": "associate producer",

-----"guessedGender": "female"

-----},

-----{

-----"Name": "Laura Vazquez",

-----"castGroup": "Produced by",

-----"order": 4,

-----"Credit": "executive producer",

-----"guessedGender": "female"

-----}
 

-----]
	
	
normalizedCrews.json

-----Crew data with guessed genders normalized for analysis and visualization.
 
 
Sources and tools used for this project:


[IMDB.com](https://www.imdb.com/)

[OMDb API](http://www.omdbapi.com/)

[gender-guesser](https://pypi.org/project/gender-guesser/) by david.arcos