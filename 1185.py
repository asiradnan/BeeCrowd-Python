b=input()
c=[]
for i in range(144):
    c.append(float(input()))
start=0
SUM=0
end=11
for k in range(11):
    for j in range(start,end):
        SUM+=c[j]
    start+=12
    end+=11
if b=='S':
    print('{:.1f}'.format(SUM))
elif b=='M':
    print('{:.1f}'.format(SUM/66))
