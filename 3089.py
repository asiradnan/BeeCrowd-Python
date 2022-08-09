while True:
    n=int(input())
    if n==0:
        break
    else:
        l=[int(i) for i in input().split()]
        SUM1=0
        SUM2=0
        SUM1=(l[0]+l[-1])
        SUM2=(l[int(len(l)/2)-1]+l[int(len(l)/2)])
        print(SUM1,SUM2)
