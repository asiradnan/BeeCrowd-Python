a=int(input())
b=input()
c=[]
for i in range(144):
    c.append(float(input()))
list2=[]
for j in range(12):
    list2.append(c[a])
    a+=12
if b=='S':
    print('{:.1f}'.format(sum(list2)))
elif b=='M':
    print('{:.1f}'.format(sum(list2)/12))
