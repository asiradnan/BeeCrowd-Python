a=[int(i) for i in input().split()]
dic={}
for J in range(a[0]):
    b=input().split()
    dic[b[0]]=int(b[1])
input()
c=input().split()
SUM=0
for K in c:
    SUM+=dic[K]
print(SUM)
if SUM>=int(a[1]):
    print('You shall pass!')
else:
    print('My precioooous')
