y=int(input())
for i in range(y):
    main=[]
    for j in range(int(input())):
        main.append(input())
    for k in range(int(input())):
        a=input()
        f=True
        for x in main:
            if x in a:
                b=a[a.find(x):]
                if len(b)>len(x):
                    index=b.find(x)+(len(x))
                    if 65<=ord(b[index])<=90 and ord(b[index])>57:
                        print('Abortar')
                        f=False
                        break
                else:
                    print('Abortar')
                    f=False
                    break 
        if f :
            print('Prossiga')
    if i!=(y-1):
        print()
