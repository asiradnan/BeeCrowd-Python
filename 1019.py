N=int(input())
a=N//3600
b=N%3600
c=b//60
d=b%60
print(a,':',c,':',d,sep="")
