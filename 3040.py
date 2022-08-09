for i in range(int(input())):
    a=[int(j) for j in input().split()]
    if 200<=a[0]<=300 and a[1]>=50 and a[2]>=150:
        print('Sim')
    else:
        print('Nao')
