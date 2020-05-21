t=int(input())
for i in range(t):
    d,n=map(int,input().split())
    ans=n
    for i in range(d):
        for i in range(n):
            ans += i
            n=ans
    print(n)
