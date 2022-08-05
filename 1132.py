X=int(input())
Y=int(input())
if X>Y:
    b=X
    a=Y
else:
    b=Y
    a=X
SUM=0
for i in range(a,b+1):
    if i%13!=0:
        SUM+=i
print(SUM)
