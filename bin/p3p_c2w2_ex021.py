#schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode.
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits=0
for c_credit in schedule:
    total_credits=total_credits+schedule[c_credit]
print(total_credits)
