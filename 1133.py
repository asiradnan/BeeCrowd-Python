X=int(input())
Y=int(input())
if X>Y:
    b=X
    a=Y
else:
    b=Y
    a=X
for i in range(a+1,b):
    if i%5==2 or i%5==3:
        print(i)
