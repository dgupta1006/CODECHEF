t=int(input())
for i in range(t):
    m,n,k=map(int,input().split())
    if(m>n):
        d=m-(n+k)
        if (d < 0):
            if (d % 2 == 0):
                d = 0
            else:
                d = 1
    elif(n>m):
        d=n-(m+k)
        if(d<0):
            if(d%2==0):
               d=0
            else:
               d=1
    else:
        if(k%2==0):
           d=0
        else:
           d=1
    print(d)