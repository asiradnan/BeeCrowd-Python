b=input()
c=[]
for i in range(144):
    c.append(float(input()))
start=12
SUM=0
end=13
for k in range(11):
    for j in range(start,end):
        SUM+=c[j]
    start+=12
    end+=13
if b=='S':
    print('{:.1f}'.format(SUM))
elif b=='M':
    print('{:.1f}'.format(SUM/66))
