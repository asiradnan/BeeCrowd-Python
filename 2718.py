output=[]
for i in range(int(input())):
    a=bin(int(input().strip()))
    a=str(a)
    a=a[2:]
    a=a.split('0')
    count=0
    for j in a:
        if len(j)>count:
            count=len(j)
    print(count)
