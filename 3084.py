while True:
    try:
        a=[int(i) for i in input().split()]
        print('{0:>02d}:{1:>02d}'.format(int(a[0]/30),int(a[1]/6)))
    except:
        break
