list1=[]
while True:
    try:
        while True:
            a=input()
            if a not in list1:
                list1.append(a)
    except:
        break
print(len(list1))
