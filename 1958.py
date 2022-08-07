a=input()
if a.startswith('-'):
    sc='{:.4E}'.format(float(a))
    print(sc)
else:
    sc='{:.4E}'.format(float(a))
    print(f'+{sc}')
