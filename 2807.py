list1=[]
a=0
b=1
x=int(input())
if x>=1:
    list1=[str(b)]
while len(list1)<x:
    c=a+b
    list1.append(str(c))
    a=b
    b=c
list1=list1[::-1]
print(' '.join(list1))
