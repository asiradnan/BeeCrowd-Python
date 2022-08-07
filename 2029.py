while True:
    try:
        n=float(input())
        p=float(input())
        pie=3.14
        r=p/2
        print('ALTURA = {:.2f}'.format(n/(pie*(r**2))))
        print('AREA = {:.2f}'.format(pie*(r**2)))
    except:
        break
