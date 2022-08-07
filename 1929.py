a=input().split()
list1=[int(i) for i in a]
count=0
one=list1[:3]
two=list1[1:]
three=list1[2:]
three.append(list1[0])
four=list1[:2]
four.append(list1[-1])
list2=[one,two,three,four]
f=False
for j in list2:
    c=max(j)
    j.remove(c)
    if c<sum(j):
        f=True
        print('S')
        break
if f==False:
    print('N')
