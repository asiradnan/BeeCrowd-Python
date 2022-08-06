a=input().split()
b=[int(i) for i in a]
x,y,z=tuple(b)
if x>y and (y<z or y==z):
    print(':)')
elif x<y and (y>z or y==z):
    print(':(')
elif x<y and y<z:
    p=abs(y-z)
    q=abs(x-y)
    if p<q:
        print(':(')
    else:
        print(':)')
elif x>y and y>z:
    p=abs(y-z)
    q=abs(x-y)
    if p<q:
        print(':)')
    else:
        print(':(')
elif x==y and y<z:
    print(':)')
elif x==y and y>=z:
    print(':(')
