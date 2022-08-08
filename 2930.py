x=[int(i) for i in input().split()]
d=x[1]
e=x[0]
if d-e>=3:
    print('Muito bem! Apresenta antes do Natal!')
elif d-e<=0:
    print('Eu odeio a professora!')
else:
    print('Parece o trabalho do meu filho!')
    f=d
    d+=2
    if d<=24:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')
