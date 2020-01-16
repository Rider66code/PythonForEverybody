#6. Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. Fix the code so that it passes the test. This should only require changing one line of code.

def waste(mar, var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string

print(waste(mar='Lol'))
