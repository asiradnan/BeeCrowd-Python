b=[int(i) for i in input().split()]
f=False
for j in b:
    if b.count(j)>1:
        f=True
        print('S')
        break
if f==False:
    c=max(b)
    b.remove(c)
    if sum(b)==c:
        print('S')
    else:
        print('N')
