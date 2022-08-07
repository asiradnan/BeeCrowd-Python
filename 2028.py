case=1
while True:
    try:
        N=int(input())
        empty=[0]
        for i in range(N+1):
            for j in range(i):
                empty.append(i)
        if len(empty)==1:
            print('Caso {0:}: {1:} numero'.format(case,len(empty)))
            case+=1
        else:
            print('Caso {0:}: {1:} numeros'.format(case,len(empty)))
            case+=1
        empty2=[str(k) for k in empty]
        print(' '.join(empty2))
        print()
    except:
        break
