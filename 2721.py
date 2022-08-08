list1=['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen','Rudolph']
a=input().split()
b=[int(i) for i in a]
b=sum(b)
print(list1[int(b%9)-1])
