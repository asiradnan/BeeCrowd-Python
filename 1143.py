N=int(input())
start=1
for i in range(N):
    for j in range(1,3):
        print(start**j,end=' ')
    print(start**3)
    start+=1
