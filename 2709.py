while True:
    try:
        list1=[]
        SUM=0
        count=0
        for i in range(int(input())):
            list1.append(int(input()))
        b=int(input())
        for j in range(len(list1)-1,-1,-(b)):
            SUM+=list1[j]
        for k in range(1,SUM+1):
            if SUM%k==0:
                count+=1
        if count==2 and SUM!=1:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except:
        break
