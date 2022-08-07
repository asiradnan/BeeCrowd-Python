while True:
    x=[7,12,22,52,102,15,25,55,105,30,60,110,70,120,150]
    a=[int(i) for i in input().split()]
    if a==[0,0]:
        break
    else:
        if a[1]-a[0] in x:
            print('possible')
        else:
            print('impossible')
