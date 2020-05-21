t=int(input())
for i in range (t):
    x,y,k,n=map(int,input().split())
    v=0
    for i in range (n):
        p,c=map(int,input().split())
        if(p>=(x-y) and c<=k):
            v+=1

    if (v>0):
        print("LuckyChef")
    else:
        print("UnluckyChef")