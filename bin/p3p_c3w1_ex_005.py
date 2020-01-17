
#nested-9-2: Say we had a JSON string in the following format. How would you convert it so that it is a python list?
entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""

 json.loads(entertainment)
