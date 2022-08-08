def ekta(b):
    valid='0123456789'
    count=0
    a=b.split('-')
    for j in a[1]:
        if j in valid:
            count+=1
    f=True
    for fd in a[0]:
        if 65<=ord(fd)<=90:
            f=True
        else:
            f=False
            break
    if len(b)!=8:
        print('FAILURE') 
    elif f==False:
        print('FAILURE')
    elif count!=4:
        print('FAILURE')
    else:
        if a[1][-1]=='0' or a[1][-1]=='9':
            print('FRIDAY')
        elif a[1][-1]=='7' or a[1][-1]=='8':
            print('THURSDAY')
        elif a[1][-1]=='5' or a[1][-1]=='6':
            print('WEDNESDAY')
        elif a[1][-1]=='3' or a[1][-1]=='4':
            print('TUESDAY')
        elif a[1][-1]=='1' or a[1][-1]=='2':
            print('MONDAY')
        else:
            print('FAILURE')
for i in range(int(input())):
    b=input().strip()
    if ('-' not in b):
        print('FAILURE')
    else:
        ekta(b)
