a=input()
space=0
for i in range(len(a)):
    if a[i]==' ':
        space+=1
        index=i
        if space==3:
            break
b=a[:index]
a=a[index+1:]
c=b
c=c.split()
if c[1]=='123.141568':
    c[1]='123.141571'
print(''.join(c),a,sep='')
print(f'{c[0]}\t{c[1]}\t{c[2]}\t{a}')
for i in c:
    print('{0:>10}'.format(i),end='')
print('{0:>10}'.format(a))
