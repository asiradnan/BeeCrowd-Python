M=int(input())
d=[int(input()),int(input())]
d.append(M-sum(d))
print(max(d))
