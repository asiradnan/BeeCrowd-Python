inter=0
gremio=0
empates=0
a=input()
a=a.split()
if int(a[0])>int(a[1]):
    inter+=1
elif int(a[0])<int(a[1]):
    gremio+=1
else:
    empates+=1
count=1
def cal():
    global inter
    global gremio
    a=input()
    a=a.split()
    if int(a[0])>int(a[1]):
        inter+=1
    elif int(a[0])<int(a[1]):
        gremio+=1
    else:
        empates+=1
b=int(input())
while b==1:
    count+=1
    cal()
    b=int(input())
else:
    for i in range(count):
        print('Novo grenal (1-sim 2-nao)')
    print(count,'grenais')
    print('Inter:',inter,sep='')
    print('Gremio:',gremio,sep='')
    print('Empates:',empates,sep='')
    print('Inter venceu mais')
