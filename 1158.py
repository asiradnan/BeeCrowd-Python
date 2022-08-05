N=int(input())
for i in range(N):
    a=input()
    list1=a.split()
    X=int(list1[0])
    Y=int(list1[1])
    count=1
    SUM=0
    while count<=Y:
        if X%2==1:
            SUM+=X
            count+=1
        X+=1
    print(SUM)
