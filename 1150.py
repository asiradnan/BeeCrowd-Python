X=int(input())
while True:
    Z=int(input())
    if Z<=X:
        continue
    else:
        break
SUM=0
count=0
for i in range(X,X+Z):
    SUM+=i
    count+=1
    if SUM>Z:
        print(count)
        break
