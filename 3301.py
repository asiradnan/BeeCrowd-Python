a=input().split()
b=[int(i) for i in a]
b.remove(max(b))
b.remove(min(b))
index=a.index(str(b[0]))
if index==0:
    print('huguinho')
elif index==1:
    print('zezinho')
elif index==2:
    print('luisinho')
