def check(w):
    if w==1:
        print('Valido-Equilatero')
    elif w==3:
        print('Valido-Escaleno') 
    else:
        print('Valido-Isoceles') 

def rectangular(x,y,z):
    if x**2+y**2==z**2:
        return 'Retangulo: S'
    elif  x**2+z**2==y**2:
        return 'Retangulo: S'
    elif  y**2+z**2==x**2:
        return 'Retangulo: S'
    else:
        return 'Retangulo: N'
b=[int(i) for i in input().split()]
x,y,z=b
def validation(x,y,z):
    f= True
    if x+y>z:
        f=True
    else:
        f=False
        return 'Invalido'
    if y+z>x:
        f=True
    else:
        f=False
        return 'Invalido'
    if x+z>y:
        f=True
    else:
        f=False
        return 'Invalido'
a=validation(x,y,z)
if a=='Invalido':
    print(a)
else:
    list2=[]
    for j in b:
        if j not in list2:
            list2.append(j)
    check(len(list2))
    print(rectangular(x,y,z))
