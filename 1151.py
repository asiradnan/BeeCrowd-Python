N=int(input())
list1=['0']
x=0
y=1
if len(list1)<N:
    list1.append(str(y))
for i in range(N):
    z=x+y
    if len(list1)<N:
        list1.append(str(z))
    else:
        break
    x=y
    y=z
print(' '.join(list1))
