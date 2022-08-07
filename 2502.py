while True:
    try:
        a=input().split()
        str1=input().lower()
        str2=input().lower()
        for i in range(int(a[1])):
            b=input()
            empty=''
            for j in b:
                if j.lower() in str1:
                    if j.lower()==j:
                        empty+=str2[str1.index(j.lower())]
                    else:
                        empty+=(str2[str1.index(j.lower())].upper())
                elif j.lower() in str2:
                    if j.lower()==j:
                        empty+=str1[str2.index(j.lower())]
                    else:
                        empty+=(str1[str2.index(j.lower())].upper())
                else:
                    empty+=j
            print(empty)
        print()
    except:
        break
