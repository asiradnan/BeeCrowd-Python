while True:
    try:
        a=input().split()
        b=[int(i) for i in a]
        x=b[2]
        b.pop(2)
        for j in range(x):
            list1=input().split()
            list2=[int(k) for k in list1]
            if max(list2)<=max(b) and min(list2)<=min(b):
                print('Sim')
            else:
                print('Nao')
    except:
        break
