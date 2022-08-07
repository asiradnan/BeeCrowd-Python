while True:
    try:
        main=[]
        a=input().split()
        for i in range(int(a[0])):
            b=input().split()
            main.append([int(j) for j in b])
        for j in range(len(main)):
            SUM=0
            if j==0:
                for k in range(len(main[j])):
                    if k==0:
                        if main[j][k+1]==1:
                            SUM+=1
                        if main[j+1][k]==1:
                            SUM+=1
                    elif k!=int(a[1]):
                        if main[j][k+1]==1:
                            SUM+=1
                        if main[j][k-1]==1:
                            SUM+=1
                        if main[j+1][k]==1:
                            SUM+=1
                    else:
                        if main[j][k-1]==1:
                            SUM+=1
                        if main[j+1][k]==1:
                            SUM+=1
                
            elif j!=int(a[0]):
                for k in range(len(main[j])):
                    if k==0:
                        if main[j][k+1]==1:
                            SUM+=1
                        if main[j+1][k]==1:
                            SUM+=1
                        if main[j-1][k]==1:
                            SUM+=1
                    elif k!=int(a[1]):
                        if main[j][k+1]==1:
                            SUM+=1
                        if main[j][k-1]==1:
                            SUM+=1
                        if main[j+1][k]==1:
                            SUM+=1
                        if main[j-1][k]==1:
                            SUM+=1
                    else:
                        if main[j][k+1]==1:
                            SUM+=1
                        if main[j][k-1]==1:
                            SUM+=1
                        if main[j-1][k]==1:
                            SUM+=1
            main[j][k]=SUM
        print(main)
    except:
        break
