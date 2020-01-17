#The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold=None
for city in nested_d:
    if city=='London':
        print(nested_d[city])
        for country in nested_d[city]:
            if country=='Great Britain':
                london_gold=nested_d[city][country]
print(london_gold)
