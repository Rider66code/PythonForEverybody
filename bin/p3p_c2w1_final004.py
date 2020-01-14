# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
fileref = open("school_prompt.txt", "r")
beginning_chars=fileref.readline()[:30]
print(beginning_chars)
fileref.close()
