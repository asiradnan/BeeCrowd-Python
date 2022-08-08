V=0
G=0
for i in range(int(input())):
    a=input().split()
    if a[0]=='V':
        V+=int(a[1])
    else:
        G+=int(a[1])
if V<G:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')
