N=int(input())
for i in range(N):
    a=input().split()
    c=[int(j) for j in input().split()]
    d=sum(c)
    if d%2==0:
        if a[1]=='PAR':
            print(a[0])
        else:
            print(a[2])
    else:
        if a[1]=='PAR':
            print(a[2])
        else:
            print(a[0])
