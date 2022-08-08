while True:
    try:
        list1=[]
        for i in range(int(input())):
            list1.append(float(input()))
        list1.sort()
        print(list1[0])
    except:
        break
