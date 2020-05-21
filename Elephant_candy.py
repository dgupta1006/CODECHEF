t=int(input())
for i in range(t):
    n,c=map(int,input().split())
    k=list(map(int,input().split()))
    if(sum(k) <=c):
        print("YES")
    else:
        print("NO")
