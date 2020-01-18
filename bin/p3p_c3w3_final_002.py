#Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.

import requests_with_caching
import json
def get_movies_from_tastedive(movie_name):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = movie_name
    params_diction["limit"] = 5
    params_diction["type"] = "movies"
    tastedive_resp = requests_with_caching.get(baseurl, params = params_diction)
    return tastedive_resp.json()

def extract_movie_titles(emt_value):
    titles=list()
    for results in emt_value.values():
        if type(results)==dict:
            for tempmovies in results['Results']:
                titles.append(tempmovies['Name'])
        print(titles)
    return titles

print(extract_movie_titles(get_movies_from_tastedive("Tony Bennett")))

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
