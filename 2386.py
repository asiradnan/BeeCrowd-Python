while True:
    dic={'suco de laranja':120,'morango fresco':85,'mamao':85,'goiaba vermelha':70,'manga':56 ,'laranja':50,'brocolis':34}
    valid='0123456789'
    T=int(input())
    SUM=0
    if T==0:
        break
    else:
        for i in range(T):
            b=input()
            string=''
            c=''
            for j in b:
                if j in valid:
                    string+=j
                else:
                    c+=j
            c=c.strip()
            SUM+=dic[c]*int(string)
    if SUM>130:
        print('Menos',SUM-130,'mg')
    elif SUM<110:
        print('Mais',110-SUM,'mg')
    else:
        print(SUM,'mg')
