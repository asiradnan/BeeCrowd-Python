a=input().split()
b=[int(i) for i in a]
empty=b[0]+b[1]
s=0
while empty>=b[2]:
    c=empty//b[2]
    s+=c
    empty=empty%b[2]
    empty+=c
print(s)
