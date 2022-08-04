a=input().split()
b=[float(i) for i in a]
p=b[0]*2
q=b[1]*3
r=b[2]*4
s=b[3]*1
m=(p+q+r+s)/10
print('Media: {:.1f}'.format(m))
if m>=7.0:
    print('Aluno aprovado.')
elif m<5.0:
    print('Aluno reprovado.')
elif 5.0<=m<7.0:
    print('Aluno em exame.')
    x=float(input())
    print('Nota do exame: {:.1f}'.format(x))
    y=(x+m)/2
    if y>=5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(y))
