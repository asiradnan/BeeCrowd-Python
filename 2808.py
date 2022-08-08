board=[['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'], ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'], ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'], ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'], ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'], ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']]
a=input().split()
x=a[0]
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col]==x:
            r=row
            c=col
            break
valid=[]
if r==0:
    if c==0:
        valid.append(board[r+2][c+1])
        valid.append(board[r+1][c+2])
    elif c==1:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c+2])
    elif c>1 and c<6:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r+1][c-2])
    elif c==6:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c-2])
    elif c==7:
        valid.append(board[r+1][c-2])
        valid.append(board[r+2][c-1])
elif r==1:
    if c==0:
        valid.append(board[r+2][c+1])
        valid.append(board[r+1][c+2])
        valid.append(board[r-1][c+2])
    elif c==1:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r-1][c+2])
    elif c>1 and c<6:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r+1][c-2])
        valid.append(board[r-1][c+2])
        valid.append(board[r-1][c-2])
    elif c==6:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c-2])
        valid.append(board[r-1][c-2])
    elif c==7:
        valid.append(board[r+1][c-2])
        valid.append(board[r+2][c-1])
        valid.append(board[r-1][c-2])
elif 1<r<6:
    if c==0:
        valid.append(board[r+2][c+1])
        valid.append(board[r+1][c+2])
        valid.append(board[r-1][c+2])
        valid.append(board[r-2][c+1])
    elif c==1:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r-1][c+2])
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
    elif c>1 and c<6:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r+1][c-2])
        valid.append(board[r-1][c+2])
        valid.append(board[r-1][c-2])
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
    elif c==6:
        valid.append(board[r+2][c+1])
        valid.append(board[r+2][c-1])
        valid.append(board[r+1][c-2])
        valid.append(board[r-1][c-2])
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
    elif c==7:
        valid.append(board[r+1][c-2])
        valid.append(board[r+2][c-1])
        valid.append(board[r-1][c-2])
        valid.append(board[r-2][c-1])
elif r==6:
    if c==0:
        valid.append(board[r-2][c+1])
        valid.append(board[r+1][c+2])
        valid.append(board[r-1][c+2])
    elif c==1:
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r-1][c+2])
    elif c>1 and c<6:
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
        valid.append(board[r+1][c+2])
        valid.append(board[r+1][c-2])
        valid.append(board[r-1][c+2])
        valid.append(board[r-1][c-2])
    elif c==6:
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
        valid.append(board[r+1][c-2])
        valid.append(board[r-1][c-2])
    elif c==7:
        valid.append(board[r+1][c-2])
        valid.append(board[r-2][c-1])
        valid.append(board[r-1][c-2])
elif r==7:
    if c==0:
        valid.append(board[r-2][c+1])
        valid.append(board[r-1][c+2])
    elif c==1:
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
        valid.append(board[r-1][c+2])
    elif c>1 and c<6:
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
        valid.append(board[r-1][c+2])
        valid.append(board[r-1][c-2])
    elif c==6:
        valid.append(board[r-2][c+1])
        valid.append(board[r-2][c-1])
        valid.append(board[r-1][c-2])
    elif c==7:
        valid.append(board[r-1][c-2])
        valid.append(board[r-2][c-1])
if a[1] in valid:
    print('VALIDO')
else:
    print('INVALIDO')
