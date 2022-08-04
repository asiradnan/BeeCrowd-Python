while True:
    X,Y=[int(i) for i in input().split()]
    if X>Y:
        print('Decrescente')
    elif Y>X:
        print('Crescente')
    else:
        break
