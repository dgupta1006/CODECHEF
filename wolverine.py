t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=0
    a=list(map(int,input().split()))
    res = [x + k for x in a]
    for j in range(len(res)):
        if (res[j]%7==0):
           s+=1
    print(s)



