t=int(input())
for i in range(t):
    n=int(input())
    count=0
    AC=list(map(int,input().split()))
    for i in range(1,len(AC)):
        if(AC[i]>AC[i-1] or AC[i]==AC[i-1]):
            count=count+1
    print(count+1)