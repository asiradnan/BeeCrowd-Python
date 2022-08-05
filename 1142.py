N=int(input())
start=1
for i in range(N):
    for j in range(start,start+3):
        print(j,end=' ')
    print('PUM')
    start+=4
