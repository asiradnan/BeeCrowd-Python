A,B,C,D=[int(i) for i in input().split()]
if A==C:
    if B==D:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif D>B:
        print(f'O JOGO DUROU 0 HORA(S) E {D-B} MINUTO(S)')
    else:
        print(f'O JOGO DUROU 23 HORA(S) E {60-B+D} MINUTO(S)')
elif C>A:
    E=C-A
    if D>B:
        print(f'O JOGO DUROU {E} HORA(S) E {D-B} MINUTO(S)')
    elif D<B:
        print(f'O JOGO DUROU {E-1} HORA(S) E {60-B+D} MINUTO(S)')
    else:
        print(f'O JOGO DUROU {E} HORA(S) E 0 MINUTO(S)')
else:
    E=24-A+C
    if D>B:
        print(f'O JOGO DUROU {E} HORA(S) E {D-B} MINUTO(S)')
    elif D<B:
        print(f'O JOGO DUROU {E-1} HORA(S) E {60-B+D} MINUTO(S)')
    else:
        print(f'O JOGO DUROU {E} HORA(S) E 0 MINUTO(S)') 
