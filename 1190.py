b=input()
c=[]
for i in range(144):
    c.append(float(input()))
start=23
SUM=0
end=24
for k in range(5):
    for j in range(start,end):
        SUM+=c[j]
    start+=11
    end+=12
st=79
en=84
for l in range(5):
    for m in range(st,en):
        SUM+=c[m]
    st+=13
    en+=12
if b=='S':
    print('{:.1f}'.format(SUM))
elif b=='M':
    print('{:.1f}'.format(SUM/30))
