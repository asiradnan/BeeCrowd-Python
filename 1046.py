A,B=[int(i) for i in input().split()]
if B>A:
    print(f'O JOGO DUROU {B-A} HORA(S)')
elif A>B:
    C=24-A
    print(f'O JOGO DUROU {B+C} HORA(S)')
else:
    print('O JOGO DUROU 24 HORA(S)')
