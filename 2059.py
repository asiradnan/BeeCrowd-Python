b=[int(i) for i in input().split()]
if b[-1]==0:
    if b[-2]==1:
        print('Jogador 1 ganha!')
    else:
        if b[0]==0:
            c=b[1]+b[2]
            if c%2==0:
                print('Jogador 2 ganha!')
            else:
                print('Jogador 1 ganha!')
        elif b[0]==1:
            c=b[1]+b[2]
            if c%2==0:
                print('Jogador 1 ganha!')
            else:
                print('Jogador 2 ganha!')
elif b[-1]==1:
    if b[-2]==1:
        print('Jogador 2 ganha!')
    else:
        print('Jogador 1 ganha!')
