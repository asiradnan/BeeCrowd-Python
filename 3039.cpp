carrinhos=0
bonecas=0
for i in range(int(input())):
    a=input().split()
    if a[1]=='M':
        carrinhos+=1
    else:
        bonecas+=1
print(f'{carrinhos} carrinhos')
print(f'{bonecas} bonecas')
