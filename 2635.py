while True:
    try:
        list1=[]
        for i in range(int(input())):
            list1.append(input())
        for k in range(int(input())):
            b=input()
            l=len(b)
            count=0
            MAX=''
            for j in list1:
                if j[:l]==b:
                    if len(j)>len(MAX):
                        MAX=j
                    count+=1
            if count==0:
                print(-1)
            else:
                print(count,len(MAX))
    except:
        break
