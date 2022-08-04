X=int(input())
SUM=0
AwSum=0
for i in range(X):
    Y=int(input())
    if 10<=Y<=20:
        SUM+=1
    else:
        AwSum+=1
print(SUM,'in')
print(AwSum,'out')
