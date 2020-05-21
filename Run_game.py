t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(max(a)>max(b) or max(b)>max(a)):
        print("YES")
    else:
        print("NO")


