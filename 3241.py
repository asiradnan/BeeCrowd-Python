for i in range(int(input())):
    a=input()
    if a=='P=NP':
        print('skipped')
    else:
        a=a.split('+')
        print(int(a[0])+int(a[1]))
