p1 = Pet("Fido")
print(p1)
for i in range(10):
    p1.clock_tick()
    print(p1)
p1.feed()
p1.hi()
p1.teach("Boo")
for i in range(10):
    p1.hi()
print(p1)
