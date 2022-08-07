n=int(input())
for i in range(n):
    name=input()
    D=float(input().strip())
    score=input().split()
    scores=[float(j) for j in score]
    scores.remove(max(scores))
    scores.remove(min(scores))
    print('{0:} {1:.2f}'.format(name,(sum(scores)*D)))
