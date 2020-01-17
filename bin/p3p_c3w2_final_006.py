#Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
#print(list(zip(l1,l2)))
#opposites=[(l11,l12) for (l11,l12) in list(zip(l1,l2)) if len(l11)>3 and len(l12)>3]
# if len(l11)<3 and len(l12)<3
#print(map(lambda dir: (dir[0],dir[1]),zip(l1,l2)))
#print(filter(lambda dir: len(dir[0])>3 and len(dir[1])>3, list(zip(l1,l2))))
#(map(x,    ))
#print(map(lambda x:(x[0],x[1]),filter(lambda dir: len(dir[0])>3 and len(dir[1])>3, list(zip(l1,l2)))))
#opposites=[(l11,l12) for (l11,l12) in list(zip(l1,l2)) if len(l11)>3 and len(l12)>3]
#opposites=[(l11,l12) for (l11,l12) in list(zip(l1,l2)) if len(l11)>3 and len(l12)>3]
opposites=map(lambda x:(x[0],x[1]),filter(lambda dir: len(dir[0])>3 and len(dir[1])>3, list(zip(l1,l2))))

#NOT PASSING YET
