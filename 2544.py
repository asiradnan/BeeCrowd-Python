while True:
    try:
        a=int(input())
        for i in range(a):
            if 2**i==a:
                print(i)
                break
    except:
        break
