while True:
    try:
        a=float(input())
        b=240*a
        def cal(a):
            b=a//3600
            c=a%3600
            d=c//60
            e=c%60
            print('{0:02d}:{1:02d}:{2:02d}'.format(int(b),int(d),int(e)))
        if a==360:
            print('Bom Dia!!')
            print('06:00:00')
        elif 0<=a<90:
            print('Bom Dia!!')
            b=240*a
            b+=(3600*6)
            cal(b)
        elif 90<=a<180:
            print("Boa Tarde!!")
            b=240*(a-90)
            b+=(3600*12)
            cal(b)
        elif 180<=a<270:
            print('Boa Noite!!')
            b=240*(a-180)
            b+=(3600*18)
            cal(b)
        else:
            print('De Madrugada!!')
            b=240*(a-270)
            cal(b)
    except:
        break
