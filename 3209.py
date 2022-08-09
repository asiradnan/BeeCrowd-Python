for i in range(int(input())):
    a=input()
    b=[int(j) for j in a[1:].split()]
    if 0 in b:
        b.remove(0)
    print(sum(b)-len(b)+1)
