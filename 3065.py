case=1
while True:
    a=int(input())
    if a==0:
        break
    else:
        b='0'+input()
        c=b
        b=b.replace('-','+')
        list1=[int(ab) for ab in b.split('+')]
        for i in c:
            if i=='+' or i=='-':
                if i=='+':
                    SUM=list1[0]+list1[1]
                    list1.pop(0)
                    list1.pop(0)
                    list1.insert(0,SUM)
                else:
                    SUM=list1[0]-list1[1]
                    list1.pop(0)
                    list1.pop(0)
                    list1.insert(0,SUM)
        print('Teste',case)
        case+=1
        print(list1[0])
        print()
