def game(bonus):
    a,b,c=[int(i) for i in input().split()]
    value=(a+b)/2
    if c%2==0:
        value+=bonus
    return value
n=int(input().strip())
for i in range(n):
    bonus=int(input().strip())
    player1=game(bonus)
    player2=game(bonus)
    if player1>player2:
        print('Dabriel')
    elif player1==player2:
        print('Empate')
    else:
        print('Guarte')
