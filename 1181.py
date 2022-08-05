a=int(input())
b=input()
c=[]
for i in range(144):
    c.append(float(input()))
c=c[(12*a):(12*(a+1))]
if b=='S':
    print('{:.1f}'.format(sum(c)))
elif b=='M':
    print('{:.1f}'.format(sum(c)/12))
