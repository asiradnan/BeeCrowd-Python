import math
a=input().split()
x=int(a[0])*int(a[1])
st=''
for i in range(1,10):
    st+=str(math.ceil(x*(i/10)))
    st+=' '
print(st[:-1])
