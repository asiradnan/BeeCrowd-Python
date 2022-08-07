a=input().split()
start=int(a[0])
for i in range(int(a[1])):
    b=input()
    if b=='fechou':
        start+=1
    else:
        start-=1
print(start)
