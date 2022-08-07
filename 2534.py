while True:
    try:
        user=input()
        list1=user.split()
        N=int(list1[0])
        grade=[]
        for i in range(N):
            grade.append(int(input()))
        grade.sort(reverse=True)
        P=int(list1[1])
        for j in range(P):
            temp=int(input())
            print(grade[temp-1])
    except:
        break
