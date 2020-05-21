t=int(input())
for i in range(t):
    n=int(input())
    w=list(map(int,input().split()))
    print(sum(w)-min(w)*len(w))