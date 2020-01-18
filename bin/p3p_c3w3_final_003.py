#Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
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
    return titles

def get_related_titles(movies):
    relatedlist=list()
    if len(movies)>0:
        for movie in movies:
            movlist=extract_movie_titles(get_movies_from_tastedive(movie))
            for movie2 in movlist:
                if movie2 not in relatedlist:
                    relatedlist.append(movie2)
    return relatedlist
    pass
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
