t=int(input())
for i in range(t):
    n=int(input())
    ans=n
    count=0
    if(n%10==0):
        count=0
    else:
        x=n%10
        if(x==5):
            count=1
        else:
            count=-1

    print(count)

