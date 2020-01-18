#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
import requests_with_caching
import json
def get_movie_data(movie_name):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction["t"] = movie_name
    params_diction["r"] = "json"
    omdb_resp = requests_with_caching.get(baseurl, params = params_diction)
    return omdb_resp.json()

get_movie_data("Deadpool 2")

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_rating(search):
    rating=0
    if type(search)==dict:
        ratelist=search["Ratings"]
        print(ratelist)
        for source in ratelist:
            if source['Source']=='Rotten Tomatoes':
                rating=int(source['Value'].replace('%',''))
    return rating
