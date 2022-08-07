while True:
    try:
        list1=[]
        a=input().split()
        f=True
        for i in range(int(a[1])):
            b=input().split()
            if b.count('1')==int(a[0]):
                list1.append(b[0])
                f=False
        if f:
            print('Pizza antes de FdI')
        else:
            print(list1[0])
    except:
        break
