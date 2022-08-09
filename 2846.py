a=2
b=3
fibonot=[]
i=int(input())
while len(fibonot)<i:
    c=a+b
    for j in range(b+1,c):
        fibonot.append(j)
    a=b
    b=c
print(fibonot[i-1])
