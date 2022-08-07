for i in range(int(input())):
    a=input().split()
    if a[-1]=='1':
        print('{0:0>2}:{1:0>2} - A porta abriu!'.format(a[0],a[1]))
    else:
        print('{0:0>2}:{1:0>2} - A porta fechou!'.format(a[0],a[1]))
