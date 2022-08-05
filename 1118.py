def cal():
    list1=[]
    while len(list1)<2:
        a=float(input())
        if 1<=a<=10:
            list1.append(a)
        else:
            print('nota invalida')
        b=float(input())
        if 1<=b<=10:
            list1.append(b)
        else:
            print('nota invalida')
    print('media = {0:.2f}'.format(sum(list1)/2))
cal()
def d():
    return float(input())
while True:
    print('novo calculo (1-sim 2-nao)')
    c=int(d())
    while c!=2 and c!=1:
        print('novo calculo (1-sim 2-nao)')
        c=d()
    if c==1:
        cal()
    elif c==2:
        break
