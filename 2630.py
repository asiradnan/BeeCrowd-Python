for i in range(int(input())):
    a=input()
    b=input().split()
    c=[int(j) for j in b]
    if a=="min":
        print(f'Caso #{i+1}: {min(c)}')
    elif a=='mean':
        print(f'Caso #{i+1}: {int(sum(c)/len(c))}')
    elif a=='max':
        print(f'Caso #{i+1}: {max(c)}')
    else:
        print(f'Caso #{i+1}: {int((.3*c[0])+(.59*c[1])+(.11*c[2]))}')
