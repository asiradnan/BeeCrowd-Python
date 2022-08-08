a=input().split()
b=input().split()
SUM=0
for i in range(len(a)):
    if int(a[i])<int(b[i]):
        SUM+=int(b[i])-int(a[i])
print(SUM)
