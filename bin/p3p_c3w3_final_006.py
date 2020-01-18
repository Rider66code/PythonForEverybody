#Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
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

def get_movie_data(movie_name):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction["t"] = movie_name
    params_diction["r"] = "json"
    omdb_resp = requests_with_caching.get(baseurl, params = params_diction)
    return omdb_resp.json()

def get_movie_rating(search):
    rating=0
    if type(search)==dict:
        ratelist=search["Ratings"]
        for source in ratelist:
            if source['Source']=='Rotten Tomatoes':
                rating=int(source['Value'].replace('%',''))
    return rating

def get_sorted_recommendations(movlist):
    ratelist=list()
    namelist=list()
    for movie in get_related_titles(movlist):
        t=movie,get_movie_rating(get_movie_data(movie))
        ratelist.append(t)
    ratelist.sort(key=lambda tup: (tup[1],tup[0]), reverse=True)
    for name in ratelist:
        namelist.append(name[0])
    return namelist

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
