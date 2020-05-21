t=int(input())
for i in range (t):
    a,b=map(int,input().split())
    p=''
    while(a>0 or b>0):
        temp=((a%10+b%10)%10)
        p=p+str(temp)
        a=a//10
        b=b//10
    print(int(p[::-1]))
