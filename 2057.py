b=[int(i) for i in input().split()]
for j in range(len(b)):
    if b[j]==0:
        b[j]=24
if sum(b)>24:
    print(sum(b)-24)
elif sum(b)==24:
    print(0)
else:
    print(sum(b))
