n=int(input())
x=0
y=0
z=0
p=0
q=0
r=0
for i in range(n):
    hudai=input()
    a=input().split()
    b=input().split()
    x+=int(b[0])
    y+=int(b[1])
    z+=int(b[2])
    p+=int(a[0])
    q+=int(a[1])
    r+=int(a[2])
print('Pontos de Saque: {:.2f} %.'.format((x/p)*100))
print('Pontos de Bloqueio: {:.2f} %.'.format((y/q)*100))
print('Pontos de Ataque: {:.2f} %.'.format((z/r)*100))
