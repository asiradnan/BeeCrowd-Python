b=input()
c=[]
for i in range(144):
    c.append(float(input()))
start=1
SUM=0
end=12
for k in range(11):
    for j in range(start,end):
        SUM+=c[j]
    start+=13
    end+=12
if b=='S':
    print('{:.1f}'.format(SUM))
elif b=='M':
    print('{:.1f}'.format(SUM/66))
