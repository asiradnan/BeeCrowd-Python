N=int(input())
start=1
for i in range(N):
    for j in range(1,3):
        print(start**j,end=' ')
    print(start**3)
    print(start,end=' ')
    for j in range(2,3):
        print((start**j)+1,end=' ')
    print((start**3)+1)   
    start+=1
