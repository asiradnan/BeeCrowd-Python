dic={}
count=1
str1='.'
str2='..'
str3='...'
st1=str1
st2=str2
st3=str3
x=97
count=1
while x<=122:
    if count==1:
        dic[st1]=chr(x)
    elif count==2:
        dic[st2]=chr(x)
    elif count==3:
        dic[st3]=chr(x)
        st1+=' '+str1
        st2+=' '+str2
        st3+=' '+str3
        count=0
    x+=1
    count+=1
while True:
    try:
        for i in range(int(input())):
            print(dic[input()])
    except:
        break
