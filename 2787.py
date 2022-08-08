f=False
g=False
a=int(input())
if a%2==0:
    f=True
a=int(input())
if a%2==0:
    g=True
if f==False and g==False:
    print(1)
elif f==False or g==False:
    print(0)
else:
    print(1)
