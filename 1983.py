N=int(input())
empty={}
for i in range(N):
    a=input().split()
    empty[int(a[0])]=float(a[1])
b=list(empty.values())
b.sort(reverse=True)
if b[0]<8:
    print('Minimum note not reached')
else:
    for key,value in empty.items():
        if value==b[0]:
            print(key)
