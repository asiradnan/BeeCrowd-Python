N=int(input())
for a in range(N):
    X,Y=[int(i) for i in input().split()]
    if X>Y:
        a=X
        b=Y
    else:
        a=Y
        b=X
    SUM=0
    for j in range(b+1,a):
        if j%2==1:
            SUM+=j
    print(SUM)
