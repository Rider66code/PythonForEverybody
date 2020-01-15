#If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.
p_names=[]
p_number=[]
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
for p_info in pokemon.items():
    p_names.append(p_info[0])
    p_number.append(p_info[1])
print(p_names)
print(p_number)
