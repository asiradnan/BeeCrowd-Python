b=input()
c=[]
for i in range(144):
    c.append(float(input()))
start=12
SUM=0
end=13
for k in range(5):
    for j in range(start,end):
        SUM+=c[j]
    start+=12
    end+=13
st=72
en=77
for l in range(5):
    for m in range(st,en):
        SUM+=c[m]
    st+=12
    en+=11
if b=='S':
    print('{:.1f}'.format(SUM))
elif b=='M':
    print('{:.1f}'.format(SUM/30))
