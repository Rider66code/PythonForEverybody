#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def countrylist(somedict):
    tmplist=[]
    counter=0
    for country,count in sorted(somedict.items(),key=lambda stat:stat[0]):
        tmplist.append(country)
    return tmplist
alphabetical=countrylist(medals)
