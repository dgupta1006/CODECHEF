t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    l= max(a,b)
    h=a+b
    print(l,h)
