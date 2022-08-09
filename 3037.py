x=int(input())
for i in range(x):
    j=0
    for y in range(3):
        a=[int(j) for j in input().split()]
        j+=(a[0]*a[1])
    m=0
    for y in range(3):
        a=[int(j) for j in input().split()]
        m+=(a[0]*a[1])
    if j>m:
        print('JOAO')
    elif m>j:
        print('MARIA')
