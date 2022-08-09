dic={}
for i in range(int(input())):
    a=input().split()
    if a[1] not in dic.keys():
        dic[a[1]]=int(a[2])
    else:
        dic[a[1]]+=int(a[2])
SUM=0
for j,k in dic.items():
    if j=='bonecos':
        SUM+=k//8
    elif j=='arquitetos':
        SUM+=k//4
    elif j=='musicos':
        SUM+=k//6
    elif j=='desenhistas':
        SUM+=k//12
print(SUM)
