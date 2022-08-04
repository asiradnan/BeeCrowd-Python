count=0
SUM=0
for i in range(6):
    a=float(input())
    if a>0:
        count+=1
        SUM+=a
print(count,'valores positivos')
print('{:.1f}'.format(SUM/count))
