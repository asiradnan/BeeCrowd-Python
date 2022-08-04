N=int(input())
C=0
R=0
S=0
for i in range(N):
    a=input()
    list1=a.split()
    if list1[1]=='C':
        C+=int(list1[0])
    elif list1[1]=='S':
        S+=int(list1[0])
    elif list1[1]=='R':
        R+=int(list1[0])
print(f'Total: {C+S+R} cobaias')
print('Total de coelhos:',C)
print('Total de ratos:',R)
print('Total de sapos:',S)
print('Percentual de coelhos: {:.2f} %'.format((C/(C+S+R))*100))
print('Percentual de ratos: {:.2f} %'.format((R/(C+S+R))*100))
print('Percentual de sapos: {:.2f} %'.format((S/(C+S+R))*100))
