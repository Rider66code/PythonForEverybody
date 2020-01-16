#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def countrylist(somedict):
    tmplist=[]
    counter=0
    for country,count in sorted(somedict.items(),key=lambda stat:stat[1],reverse=True):
        if counter<3:
            counter+=1
            tmplist.append(country)
    return tmplist
top_three=countrylist(medals)
