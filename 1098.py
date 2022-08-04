I=0
while I<=1.8:
    for i in range(3):
        J=1
        J+=I+i
        if I==0 or I==1 or I==2:
            I=int(I)
            J=int(J)
            print(f'I={I} J={J}')
        else:
            print('I={0:.1f} J={1:.1f}'.format(I,J))
    I+=.2
print(f'I=2 J=3\nI=2 J=4\nI=2 J=5')
