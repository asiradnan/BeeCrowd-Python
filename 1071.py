X=int(input())
Y=int(input())
SUM=0
for i in range(Y+1,X):
    if i%2==1:
        SUM+=i
print(SUM)
