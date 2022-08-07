N=int(input())
for i in range(N):
    a=int(input())
    if a==2015:
        print('1 A.C.')
    elif a>2015:
        print(a+1-2015,'A.C.')
    else:
        print(2015-a,'D.C.')
