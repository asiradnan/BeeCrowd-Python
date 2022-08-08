dic={'Hobbit(s)':0,'Humano(s)':0,'Elfo(s)':0,'Anao(oes)':0,'Mago(s)':0}
for i in range(int(input())):
    a=input().split()
    if a[1]=='X':
        dic['Hobbit(s)']+=1
    elif a[1]=='H':
        dic['Humano(s)']+=1
    elif a[1]=='E':
        dic['Elfo(s)']+=1
    elif a[1]=='A':
        dic['Anao(oes)']+=1
    elif a[1]=='M':
        dic['Mago(s)']+=1
for key,value in dic.items():
    print(value,key)
