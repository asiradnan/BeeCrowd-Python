a=[0,0,0]
z=['A','B','C']
x=int(input())
b=input()
if b=='A':
    a[0]=1
elif b=='B':
    a[1]=1
elif b=='C':
    a[2]=1
for i in range(x):
    y=int(input())
    if y==1:
        temp=a[0]
        a[0]=a[1]
        a[1]=temp
    if y==2:
        temp=a[1]
        a[1]=a[2]
        a[2]=temp
    if y==3:
        temp=a[0]
        a[0]=a[2]
        a[2]=temp
print(z[a.index(1)])
