# Welcome Dmitrii Samodurov from Using Python to Access Web Data
#
# Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_352185.json (Sum ends with 20)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format
# The data consists of a number of names and comment counts in JSON as follows:
#
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.
#
# Sample Execution
#
# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...
import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL: ')
print('Retrieving', url)
urlhandler = urllib.request.urlopen(url, context=ctx)
data = urlhandler.read().decode()
print('Retrieved', len(data), 'characters')
count=0
total=0

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('==== Failure To Retrieve ====')
    print(data)
    quit()

#print(json.dumps(js, indent=4))
for commcount in js['comments']:
    #print(commcount)
    for key in commcount:
        if key == 'count':
            print(commcount[key])
            total=total+int(commcount[key])
    count=count+1
print('Count:',count)
print('Total:',total)
#comms=js['comments']
#print(comms)
