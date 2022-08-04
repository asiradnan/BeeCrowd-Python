list1=[]
a=input().split()
a=int(a[1])
b=input().split(' : ')
c=input().split()
c=int(c[1])
d=input().split(' : ')
f=[int(j) for j in b]
e=[int(i) for i in d]
if e[-1]-f[-1]<0:
    list1.append(e[-1]-f[-1]+60)
    e[-2]=e[-2]-1
else:
    list1.append(e[-1]-f[-1])
if e[-2]-f[-2]<0:
    list1.append(e[-2]-f[-2]+60)
    e[-3]=e[-3]-1
else:
    list1.append(e[-2]-f[-2])
if e[-3]-f[-3]<0:
    list1.append(e[-3]-f[-3]+24)
    c=c-1
else:
    list1.append(e[-3]-f[-3])
list1.append(c-a)
print(f'{list1[-1]} dia(s)\n{list1[-2]} hora(s)\n{list1[-3]} minuto(s)\n{list1[-4]} segundo(s)')
