while True:
    try:
        main=[]
        a=input().split()
        for i in range(int(a[0])):
            b=input().split()
            main.append([int(j) for j in b])
        for row in range(len(main)):
            empty=''
            for col in range(len(main[row])):
                count=0
                if main[row][col]==0:
                    if len(main)-1==0:
                        if col==0:
                            if main[row][col+1]==1:
                                count+=1
                        elif col!=0 and col!=(len(main[row])-1):
                            if main[row][col+1]==1:
                                count+=1
                            if main[row][col-1]==1:
                                count+=1
                        else:
                            if main[row][col-1]==1:
                                count+=1
                    elif row==0:
                        if col==0:
                            if main[row][col+1]==1:
                                count+=1
                            if main[row+1][col]==1:
                                count+=1
                        elif col!=0 and col!=(len(main[row])-1):
                            if main[row][col+1]==1:
                                count+=1
                            if main[row+1][col]==1:
                                count+=1
                            if main[row][col-1]==1:
                                count+=1
                        else:
                            if main[row][col-1]==1:
                                count+=1
                            if main[row+1][col]==1:
                                count+=1
                    elif row!=0 and row!=(len(main)-1):
                        if col==0:
                            if main[row][col+1]==1:
                                count+=1
                            if main[row+1][col]==1:
                                count+=1
                            if main[row-1][col]==1:
                                count+=1
                        elif col!=0 and col!=(len(main[row])-1):
                            if main[row][col+1]==1:
                                count+=1
                            if main[row+1][col]==1:
                                count+=1
                            if main[row-1][col]==1:
                                count+=1
                            if main[row][col-1]==1:
                                count+=1
                        else:
                            if main[row][col-1]==1:
                                count+=1
                            if main[row+1][col]==1:
                                count+=1
                            if main[row-1][col]==1:
                                count+=1
                    elif row==(len(main)-1):
                        if col==0:
                            if main[row][col+1]==1:
                                count+=1
                            if main[row-1][col]==1:
                                count+=1
                        elif col!=0 and col!=(len(main[row])-1):
                            if main[row][col+1]==1:
                                count+=1
                            if main[row-1][col]==1:
                                count+=1
                            if main[row][col-1]==1:
                                count+=1
                        else:
                            if main[row][col-1]==1:
                                count+=1
                            if main[row-1][col]==1:
                                count+=1
                else:
                    count='9'
                empty+=str(count)
            print(empty)
    except:
        break
