try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception, e:
    print("got an error")
    print(e)

print("continuing")
